from prospeccao.aggregator import ProspectionAggregator
from prospeccao.connectors import BaseConnector
from prospeccao.data_models import Company


class DummyConnector(BaseConnector):
    def __init__(self, name: str, companies: list[Company]):
        self.name = name
        self._companies = companies

    def search(self, category: str, location: str):
        return self._companies


def test_search_merges_duplicates_by_name():
    connector_a = DummyConnector(
        "fonte_a",
        [
            Company(
                name="Loja Duplicada",
                category="padaria",
                location="SP",
                website="https://loja.com",
                source="fonte_a",
            )
        ],
    )
    connector_b = DummyConnector(
        "fonte_b",
        [
            Company(
                name="Loja Duplicada",
                category="padaria",
                location="SP",
                whatsapp="+5511999999999",
                source="fonte_b",
            ),
            Company(
                name="Loja Única",
                category="padaria",
                location="SP",
                source="fonte_b",
            ),
        ],
    )

    aggregator = ProspectionAggregator([connector_a, connector_b])

    results = aggregator.search("padaria", "SP")

    assert len(results) == 2
    merged = next(c for c in results if c.name == "Loja Duplicada")
    assert merged.website == "https://loja.com"
    assert merged.whatsapp == "+5511999999999"
    assert merged.source == "fonte_a, fonte_b"
