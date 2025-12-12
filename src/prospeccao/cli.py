import argparse
from pathlib import Path

from .aggregator import ProspectionAggregator
from .export import export_to_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prospecção de empresas por segmento e localização.",
    )
    parser.add_argument("categoria", help="Segmento ou ramo de atividade a ser pesquisado.")
    parser.add_argument("localizacao", help="Cidade ou estado para filtrar os resultados.")
    parser.add_argument(
        "--saida",
        type=Path,
        default=Path("leads.csv"),
        help="Caminho do arquivo CSV de saída (padrão: leads.csv).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    aggregator = ProspectionAggregator()
    leads = aggregator.search(args.categoria, args.localizacao)
    path = export_to_csv(leads, args.saida)
    print(f"Arquivo gerado em: {path.resolve()}")
    print(f"Total de leads: {len(leads)}")


if __name__ == "__main__":
    main()
