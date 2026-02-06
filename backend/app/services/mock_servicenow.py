import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

from app.config import settings


@dataclass
class MockServiceNowStore:
    incidents: List[Dict]
    service_requests: List[Dict]

    @classmethod
    def load(cls) -> "MockServiceNowStore":
        base = Path(settings.data_dir)
        incidents = json.loads((base / "incidents.json").read_text())
        service_requests = json.loads((base / "service_requests.json").read_text())
        return cls(incidents=incidents, service_requests=service_requests)

    def list_incidents(self) -> List[Dict]:
        return self.incidents

    def list_service_requests(self) -> List[Dict]:
        return self.service_requests

    def update_incident(self, incident_id: str, payload: Dict) -> Dict:
        for incident in self.incidents:
            if incident["id"] == incident_id:
                incident.update(payload)
                return incident
        raise KeyError(f"Incident {incident_id} not found")

    def add_resolution(self, incident_id: str, resolution: str) -> Dict:
        return self.update_incident(
            incident_id,
            {"status": "Resolved", "resolution": resolution},
        )
