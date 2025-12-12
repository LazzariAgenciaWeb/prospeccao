from abc import ABC, abstractmethod
from typing import List

from .data_models import Company


class BaseConnector(ABC):
    """Interface para conectores de origem."""

    name: str

    @abstractmethod
    def search(self, category: str, location: str) -> List[Company]:
        """Retorna uma lista de empresas com base no segmento e local."""


class GoogleSearchConnector(BaseConnector):
    name = "google_search"

    def search(self, category: str, location: str) -> List[Company]:
        return [
            Company(
                name="Exemplo Loja A",
                category=category,
                location=location,
                website="https://exemplo-a.com",
                source=self.name,
            ),
        ]


class GoogleMapsConnector(BaseConnector):
    name = "google_maps"

    def search(self, category: str, location: str) -> List[Company]:
        return [
            Company(
                name="Exemplo Loja A",
                category=category,
                location=location,
                address="Av. Principal, 123",
                whatsapp="+5511999999999",
                source=self.name,
            ),
            Company(
                name="Exemplo Loja B",
                category=category,
                location=location,
                address="Rua Secundária, 45",
                instagram="https://instagram.com/exemplo_b",
                source=self.name,
            ),
        ]


class InstagramConnector(BaseConnector):
    name = "instagram"

    def search(self, category: str, location: str) -> List[Company]:
        return [
            Company(
                name="Exemplo Loja B",
                category=category,
                location=location,
                instagram="https://instagram.com/exemplo_b",
                source=self.name,
            ),
        ]


class LinkedInConnector(BaseConnector):
    name = "linkedin"

    def search(self, category: str, location: str) -> List[Company]:
        return [
            Company(
                name="Exemplo Loja C",
                category=category,
                location=location,
                linkedin="https://linkedin.com/company/exemplo-c",
                email="contato@exemplo-c.com",
                source=self.name,
            ),
        ]
