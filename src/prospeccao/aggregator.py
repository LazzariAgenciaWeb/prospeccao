from collections import defaultdict
from typing import Iterable, List

from .connectors import (
    BaseConnector,
    GoogleMapsConnector,
    GoogleSearchConnector,
    InstagramConnector,
    LinkedInConnector,
)
from .data_models import Company


class ProspectionAggregator:
    """Orquestra consultas nos conectores e normaliza os resultados."""

    def __init__(self, connectors: Iterable[BaseConnector] | None = None) -> None:
        self.connectors = list(connectors) if connectors else self._default_connectors()

    def _default_connectors(self) -> List[BaseConnector]:
        return [
            GoogleSearchConnector(),
            GoogleMapsConnector(),
            InstagramConnector(),
            LinkedInConnector(),
        ]

    def search(self, category: str, location: str) -> List[Company]:
        grouped: dict[str, Company] = {}
        alternatives: defaultdict[str, list[Company]] = defaultdict(list)

        for connector in self.connectors:
            for company in connector.search(category, location):
                key = company.name.lower().strip()
                if key in grouped:
                    grouped[key] = grouped[key].merge(company)
                else:
                    grouped[key] = company
                alternatives[key].append(company)

        return list(grouped.values())


__all__ = [
    "ProspectionAggregator",
]
