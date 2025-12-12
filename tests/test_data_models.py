from prospeccao.data_models import Company


def test_merge_prefers_existing_values_and_concatenates_sources():
    base = Company(
        name="Exemplo Loja A",
        category="restaurante",
        location="São Paulo",
        website="https://exemplo.com",
        source="google_search",
    )
    other = Company(
        name="Exemplo Loja A",
        category="restaurante",
        location="São Paulo",
        instagram="https://instagram.com/exemplo",
        source="google_maps",
    )

    merged = base.merge(other)

    assert merged.website == base.website
    assert merged.instagram == other.instagram
    assert merged.source == "google_maps, google_search"
