# Prospecção

Ferramenta inicial para prospecção de empresas por segmento e região. A solução está preparada para integrar diferentes fontes (Google Search, Google Maps, Instagram e LinkedIn) e consolidar os dados em um CSV que pode ser aberto no Excel.

> **Atenção**: nesta versão os conectores retornam dados de exemplo para demonstrar a arquitetura. As integrações reais precisam ser implementadas conforme as políticas de uso das plataformas.

## Como funciona
1. A CLI recebe o segmento (categoria) e a localização (cidade/estado).
2. Cada conector busca empresas na sua fonte e retorna os dados normalizados.
3. O agregador mescla resultados duplicados e consolida os campos (site, Instagram, LinkedIn, WhatsApp, e-mail e endereço completo).
4. Os leads são exportados para um arquivo CSV pronto para o Excel.

### Estrutura do código
- `src/prospeccao/data_models.py`: modelo de empresa e regra de mesclagem de dados duplicados.
- `src/prospeccao/connectors.py`: conectores para cada fonte (mockados nesta versão).
- `src/prospeccao/aggregator.py`: orquestra as buscas e unifica os resultados.
- `src/prospeccao/export.py`: exportação para CSV.
- `src/prospeccao/cli.py`: interface de linha de comando.

## Como executar

```bash
PYTHONPATH=src python -m prospeccao.cli "restaurantes" "São Paulo"
```

O comando gera um arquivo `leads.csv` na pasta atual, com colunas para nome, categoria, localização, site, Instagram, LinkedIn, WhatsApp, e-mail, endereço e fonte.

## Próximos passos sugeridos
- Implementar conectores reais com autenticação e respeito às políticas de uso das plataformas.
- Adicionar filtros opcionais (UF, cidade, paginação e limitação de resultados).
- Criar testes automatizados e validação de campos obrigatórios.
- Permitir exportação em formatos adicionais (XLSX/Google Sheets) e integração direta com CRM.
- Incluir cache e registro de atividade para acompanhar status das consultas.
