# Gera os dados SIMULADOS de pressão arterial usados na aula-amostra.
# Desenho: ratos hipertensos tratados com dois fármacos (A e B) em três doses
# (1, 3 e 10 mg/kg), 10 animais por grupo, um animal por medida.
# As médias por grupo foram escolhidas para fins didáticos; não são dados reais.

set.seed(1)

medias <- c(A_1 = 176, A_3 = 160, A_10 = 141,
            B_1 = 187, B_3 = 168, B_10 = 144)   # mmHg
desvio <- 9                                     # mmHg, igual em todos os grupos
n_por_grupo <- 10

largo <- as.data.frame(lapply(medias, function(m) round(rnorm(n_por_grupo, m, desvio))))
names(largo) <- names(medias)

# Formato largo: um grupo por coluna, como os dados costumam ser digitados.
# Este é o arquivo publicado no Zenodo (DOI 10.5281/zenodo.24328555).
write.csv(largo, "data/pressao_largo.csv", row.names = FALSE, quote = FALSE)

# Formato tidy: uma linha por animal, uma coluna por variável
tidy <- data.frame(
  farmaco = rep(sub("_.*", "", names(largo)), each = n_por_grupo),
  dose    = rep(as.numeric(sub(".*_", "", names(largo))), each = n_por_grupo),
  pas     = unlist(largo, use.names = FALSE)
)
write.csv(tidy, "data/pressao.csv", row.names = FALSE, quote = FALSE)
