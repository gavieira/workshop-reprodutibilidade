# Pesquisa reprodutível na prática: workshop para programas de pós-graduação

Materiais de um workshop sobre pesquisa reprodutível e ciência aberta para programas de pós-graduação das ciências da vida e da saúde.

O workshop é presencial, com duração de dois dias, e leva discentes e docentes a incorporar práticas de pesquisa aberta e reprodutível ao próprio trabalho: do planejamento do estudo ao compartilhamento de dados, código e resultados.

> **Em desenvolvimento.** Por ora, este repositório contém a aula-amostra do bloco *Da planilha ao script*. O notebook completo, com exercícios, e os materiais dos demais blocos serão adicionados.

## Materiais

| Material | Descrição | Abrir |
|---|---|---|
| [`da_planilha_ao_script_amostra.ipynb`](notebooks/da_planilha_ao_script_amostra.ipynb) | Aula-amostra: da análise por cliques a um notebook reprodutível em R (leitura de dados, arrumação no formato tidy com `tidyr`, resumo com `dplyr`, gráfico, teste t e registro da sessão) | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gavieira/workshop-reprodutibilidade/blob/main/notebooks/da_planilha_ao_script_amostra.ipynb) [![Abrir no Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gavieira/workshop-reprodutibilidade/HEAD?labpath=notebooks%2Fda_planilha_ao_script_amostra.ipynb) |

## Dados

Os dados usados na aula são **simulados**, criados para o workshop. Não são resultados de experimentos reais.

Seguindo a prática que o workshop ensina, **dados e código são publicados separadamente**: os dados estão no Zenodo, com DOI e licença CC BY; o notebook e os scripts estão aqui.

| Arquivo | Onde está | Descrição |
|---|---|---|
| `pressao_largo.csv` | Zenodo: [10.5281/zenodo.24328555](https://doi.org/10.5281/zenodo.24328555) | Pressão arterial sistólica (mmHg) de 60 ratos hipertensos tratados com um de dois fármacos (`A`, `B`) em uma de três doses (1, 3 e 10 mg/kg), 10 animais por grupo. Um grupo por coluna (`A_1`, `B_10` etc.), como os dados costumam ser digitados. É o ponto de partida da aula. |

Os scripts que geram os dados simulados estão na pasta [`scripts/`](scripts/). O notebook lê os dados diretamente pela URL do Zenodo, de modo que a análise pode ser reproduzida sem baixar nada.

## Como usar

### No Google Colab (sem instalar nada)

1. Clique no botão **Abrir no Colab** na tabela acima.
2. Confira se o ambiente é R: **Ambiente de execução → Alterar o tipo de ambiente de execução → R**.
3. Rode as células na ordem, com **Shift + Enter**.

O ambiente de R do Colab já traz os pacotes usados instalados. As versões, porém, são definidas pelo Google e mudam com o tempo.

### No Binder (sem conta e com ambiente fixo)

1. Clique no botão **Abrir no Binder** na tabela acima.
2. Aguarde a montagem do ambiente. Na primeira vez, pode levar alguns minutos.
3. Rode as células na ordem, com **Shift + Enter**.

O Binder monta o ambiente a partir dos arquivos da pasta [`binder/`](binder/): a versão do R e a data de referência dos pacotes (`runtime.txt`) e os pacotes instalados (`install.R`). Assim, o ambiente também fica registrado e versionado junto com o código. A sessão é temporária: baixe o que quiser guardar antes de fechar.

### No seu computador

1. Instale o [R](https://cran.r-project.org/) e, se preferir, o [RStudio](https://posit.co/download/rstudio-desktop/).
2. Instale os pacotes usados:

   ```r
   install.packages(c("readr", "dplyr", "tidyr", "ggplot2"))
   ```

3. Abra o notebook no Jupyter (com o kernel do R, [IRkernel](https://irkernel.github.io/)) ou no VS Code.

### Teste de reprodutibilidade

Antes de compartilhar um notebook, use **Reiniciar e executar tudo** (no Jupyter: *Kernel → Restart & Run All*). Se ele rodar do início ao fim numa sessão limpa e produzir os mesmos resultados, passou no teste.

## Licença

- **Material didático** (notebooks, README e demais textos): [CC BY 4.0](LICENSE-CONTENT.md).
- **Software** (scripts e configuração): [MIT](LICENSE).
- **Dados:** publicados no Zenodo, sob CC BY 4.0.

Detalhes em [`LICENSE-CONTENT.md`](LICENSE-CONTENT.md).

Você pode reutilizar e adaptar os materiais livremente, inclusive em outros cursos e workshops, desde que cite a fonte.

## Como citar

Use o botão **Cite this repository**, no menu lateral do GitHub, ou:

> Vieira, G. A. (2026). *Pesquisa reprodutível na prática: workshop para programas de pós-graduação* [Material didático]. https://github.com/gavieira/workshop-reprodutibilidade
