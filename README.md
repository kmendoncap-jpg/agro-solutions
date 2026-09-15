# FarmTech Solutions — Agro Solutions

Trabalho da disciplina de IA (1º período) da FIAP: aplicação de Agricultura Digital para a startup fictícia **FarmTech Solutions**.

## Culturas escolhidas

- **Soja** — cálculo de área por retângulo (base x altura) e manejo de herbicida.
- **Arroz** — cálculo de área por círculo (pivô central) e manejo de ureia.

## Arquivos do projeto

| Arquivo | Descrição |
|---|---|
| `arquivo_codigos_python.py` | Aplicação principal em Python: menu com entrada, saída (relatório), atualização e deleção de dados, usando loop e estruturas de decisão. A cada alteração, os dados são exportados para `dados_agro.csv`. |
| `arquivo_codigos_r.r` | Aplicação em R que lê `dados_agro.csv` (gerado pelo Python) e calcula média e desvio padrão das áreas plantadas. Também consulta a API pública Open-Meteo e exibe os dados climáticos atuais no terminal (item "Ir além"). |
| `dados_agro.csv` | Gerado automaticamente ao rodar o programa em Python — não deve ser editado manualmente. |

## Como executar

1. Rode o programa em Python e cadastre ao menos um registro (opção 1 do menu):
   ```
   python3 arquivo_codigos_python.py
   ```
2. Em seguida, rode o script em R na mesma pasta, para calcular as estatísticas a partir dos dados gerados:
   ```
   Rscript arquivo_codigos_r.r
   ```

## Equipe

Projeto desenvolvido em grupo, com versionamento colaborativo via GitHub, simulando um ambiente de desenvolvimento em equipe.
