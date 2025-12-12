import csv
from pathlib import Path
from typing import Iterable

from .data_models import Company


def export_to_csv(leads: Iterable[Company], output_path: str | Path) -> Path:
    """Exporta a lista de leads para um arquivo CSV."""

    path = Path(output_path)
    fieldnames = [
        "name",
        "category",
        "location",
        "website",
        "instagram",
        "linkedin",
        "whatsapp",
        "email",
        "address",
        "source",
    ]

    with path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for lead in leads:
            writer.writerow({field: getattr(lead, field) for field in fieldnames})

    return path


__all__ = ["export_to_csv"]
