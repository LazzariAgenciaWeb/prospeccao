from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Company:
    """Representa um lead retornado pelos conectores."""

    name: str
    category: str
    location: str
    website: Optional[str] = None
    instagram: Optional[str] = None
    linkedin: Optional[str] = None
    whatsapp: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    source: str = field(default="desconhecido")

    def merge(self, other: "Company") -> "Company":
        """Mescla dados de dois registros referentes à mesma empresa."""

        return Company(
            name=self.name or other.name,
            category=self.category or other.category,
            location=self.location or other.location,
            website=self.website or other.website,
            instagram=self.instagram or other.instagram,
            linkedin=self.linkedin or other.linkedin,
            whatsapp=self.whatsapp or other.whatsapp,
            email=self.email or other.email,
            address=self.address or other.address,
            source=", ".join(sorted({self.source, other.source})),
        )
