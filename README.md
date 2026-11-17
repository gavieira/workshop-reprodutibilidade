# Pesquisa reprodutível na prática: workshop para programas de pós-graduação

Materiais de um workshop sobre pesquisa reprodutível e ciência aberta para programas de pós-graduação das ciências da vida e da saúde.

O workshop é presencial, com duração de dois dias, e leva discentes e docentes a incorporar práticas de pesquisa aberta e reprodutível ao próprio trabalho: do planejamento do estudo ao compartilhamento de dados, código e resultados.

> **Em desenvolvimento.** Por ora, este repositório contém a aula-amostra do bloco *Da planilha ao script*. O notebook completo, com exercícios, e os materiais dos demais blocos serão adicionados.

## Materiais

| Material | Descrição | Abrir |
|---|---|---|
| [`da_planilha_ao_script_amostra.ipynb`](notebooks/da_planilha_ao_script_amostra.ipynb) | Aula-amostra: da análise por cliques a um notebook reprodutível em R (leitura de dados, `dplyr`, gráfico, teste t e registro da sessão) | [![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gavieira/workshop-reprodutibilidade/blob/main/notebooks/da_planilha_ao_script_amostra.ipynb) [![Abrir no Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gavieira/workshop-reprodutibilidade/HEAD?labpath=notebooks%2Fda_planilha_ao_script_amostra.ipynb) |

## Dados

| Arquivo | Descrição |
|---|---|
| [`data/toothgrowth.csv`](data/toothgrowth.csv) | Comprimento dos odontoblastos de 60 porquinhos-da-índia que receberam vitamina C em três doses (0,5, 1 e 2 mg/dia), por suco de laranja (`OJ`) ou ácido ascórbico (`VC`). Exportado do conjunto `ToothGrowth`, do pacote `datasets` do R. |

Os notebooks leem os dados diretamente pela URL do arquivo no GitHub, de modo que a análise pode ser reproduzida sem baixar nada.

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
   install.packages(c("readr", "dplyr", "ggplot2"))
   ```

3. Abra o notebook no Jupyter (com o kernel do R, [IRkernel](https://irkernel.github.io/)) ou no VS Code.

### Teste de reprodutibilidade

Antes de compartilhar um notebook, use **Reiniciar e executar tudo** (no Jupyter: *Kernel → Restart & Run All*). Se ele rodar do início ao fim numa sessão limpa e produzir os mesmos resultados, passou no teste.

## Licença

- **Código:** [MIT](LICENSE).
- **Textos e materiais didáticos:** [CC BY 4.0](LICENSE-CONTENT.md).

Você pode reutilizar e adaptar os materiais livremente, inclusive em outros cursos e workshops, desde que cite a fonte.

## Como citar

Use o botão **Cite this repository**, no menu lateral do GitHub, ou:

> Vieira, G. A. (2026). *Pesquisa reprodutível na prática: workshop para programas de pós-graduação* [Material didático]. https://github.com/gavieira/workshop-reprodutibilidade
