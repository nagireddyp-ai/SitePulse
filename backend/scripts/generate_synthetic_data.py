import json
from pathlib import Path

INCIDENTS = [
    {
        "id": "INC-1001",
        "title": "Linux server disk usage spike",
        "description": "Root partition at 95% after log rotation failed.",
        "status": "Open",
        "priority": "P2",
        "sla_timer": 4,
        "category": "Linux",
        "sla_breach": False,
    },
    {
        "id": "INC-1002",
        "title": "SSH authentication failing",
        "description": "Users cannot SSH after PAM update. Error: authentication failure.",
        "status": "In Progress",
        "priority": "P1",
        "sla_timer": 2,
        "category": "Linux",
        "sla_breach": True,
    },
    {
        "id": "INC-1003",
        "title": "High CPU on nginx host",
        "description": "Nginx process consuming 300% CPU due to runaway worker.",
        "status": "Resolved",
        "priority": "P3",
        "sla_timer": 1,
        "category": "Linux",
        "sla_breach": False,
        "resolution": "Restarted nginx and deployed rate limiting.",
    },
]

SERVICE_REQUESTS = [
    {
        "id": "SR-2001",
        "title": "Provision new Ubuntu VM",
        "description": "Need a 4-core VM for staging environment.",
        "status": "Open",
        "priority": "P3",
        "sla_timer": 8,
    },
    {
        "id": "SR-2002",
        "title": "Install monitoring agent",
        "description": "Install and configure node exporter on db node.",
        "status": "In Progress",
        "priority": "P2",
        "sla_timer": 6,
    },
]

LINUX_DOCS = [
    {
        "id": "doc-1",
        "title": "Log rotation troubleshooting",
        "content": "Symptoms: /var/log grows rapidly. Check logrotate status and permissions. Verify cron/systemd timer.",
    },
    {
        "id": "doc-2",
        "title": "SSH auth failures",
        "content": "Inspect /var/log/auth.log. Validate PAM configs and ensure sshd_config is intact.",
    },
]


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2))


def main() -> None:
    output_dir = Path("backend/data")
    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / "incidents.json", INCIDENTS)
    write_json(output_dir / "service_requests.json", SERVICE_REQUESTS)
    write_json(output_dir / "linux_docs.json", LINUX_DOCS)


if __name__ == "__main__":
    main()
