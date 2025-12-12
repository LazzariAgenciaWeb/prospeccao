import csv
from pathlib import Path

from prospeccao.data_models import Company
from prospeccao.export import export_to_csv


def test_export_to_csv_creates_file_with_expected_headers(tmp_path: Path):
    leads = [
        Company(name="Loja Teste", category="pet shop", location="RJ", source="teste"),
    ]

    csv_path = export_to_csv(leads, tmp_path / "leads.csv")

    assert csv_path.exists()
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.reader(f)
        headers = next(reader)
        assert headers == [
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
        row = next(reader)
        assert row[0] == "Loja Teste"
        assert row[-1] == "teste"
