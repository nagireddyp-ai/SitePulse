from typing import Dict

from app.services.mock_servicenow import MockServiceNowStore


class ItsmSyncAgent:
    def __init__(self, store: MockServiceNowStore) -> None:
        self.store = store

    def sync_resolution(self, incident_id: str, resolution: str) -> Dict:
        return self.store.add_resolution(incident_id, resolution)
