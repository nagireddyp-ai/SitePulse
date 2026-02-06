from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.agents.incident_analysis import IncidentAnalysisAgent
from app.agents.itsm_sync import ItsmSyncAgent
from app.agents.knowledge_generation import KnowledgeGenerationAgent
from app.agents.rag_chat import RagChatAgent
from app.llm.ollama_client import OllamaClient
from app.rag.vector_store import VectorStore
from app.services.mock_servicenow import MockServiceNowStore

app = FastAPI(title="SitePulse API")

store = MockServiceNowStore.load()
llm = OllamaClient()
vector_store = VectorStore()
incident_agent = IncidentAnalysisAgent(llm)
kb_agent = KnowledgeGenerationAgent(llm)
rag_agent = RagChatAgent(llm, vector_store)
itsm_agent = ItsmSyncAgent(store)


class ChatRequest(BaseModel):
    question: str


class IncidentUpdate(BaseModel):
    status: str


class ResolutionRequest(BaseModel):
    incident_id: str
    resolution: str


class KbRequest(BaseModel):
    incident_id: str
    resolution: str


@app.get("/incidents")
async def list_incidents():
    return {"incidents": store.list_incidents()}


@app.post("/incidents/{incident_id}")
async def update_incident(incident_id: str, payload: IncidentUpdate):
    try:
        updated = store.update_incident(incident_id, payload.dict())
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return {"incident": updated}


@app.post("/generate-kb")
async def generate_kb(payload: KbRequest):
    incident = next((i for i in store.list_incidents() if i["id"] == payload.incident_id), None)
    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    article = kb_agent.generate_article(incident, payload.resolution)
    vector_store.upsert_documents([article])
    return {"article": article}


@app.post("/chat")
async def chat(payload: ChatRequest):
    return rag_agent.answer(payload.question)


@app.get("/dashboard-metrics")
async def dashboard_metrics():
    incidents = store.list_incidents()
    total = len(incidents)
    resolved = len([i for i in incidents if i["status"] == "Resolved"])
    open_items = total - resolved
    sla_breaches = len([i for i in incidents if i.get("sla_breach")])
    priority_distribution = {
        "P1": len([i for i in incidents if i["priority"] == "P1"]),
        "P2": len([i for i in incidents if i["priority"] == "P2"]),
        "P3": len([i for i in incidents if i["priority"] == "P3"]),
        "P4": len([i for i in incidents if i["priority"] == "P4"]),
    }
    return {
        "total_incidents": total,
        "resolved": resolved,
        "open": open_items,
        "sla_breaches": sla_breaches,
        "priority_distribution": priority_distribution,
    }


@app.post("/sync-servicenow")
async def sync_servicenow(payload: ResolutionRequest):
    try:
        updated = itsm_agent.sync_resolution(payload.incident_id, payload.resolution)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return {"incident": updated}


@app.post("/analyze-incident/{incident_id}")
async def analyze_incident(incident_id: str):
    incident = next((i for i in store.list_incidents() if i["id"] == incident_id), None)
    if incident is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    analysis = incident_agent.analyze(incident)
    return {"analysis": analysis}
