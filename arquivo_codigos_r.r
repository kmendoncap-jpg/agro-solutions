install.packages("httr", quiet = TRUE)
install.packages("jsonlite", quiet = TRUE)
library(httr)
library(jsonlite)

cat("\n==================================\n")
cat("   FARMTECH SOLUTIONS - ESTATÍSTICA\n")
cat("==================================\n\n")

arquivo_dados <- "dados_agro.csv"

if (file.exists(arquivo_dados)) {
  dados_csv <- read.csv(arquivo_dados, stringsAsFactors = FALSE)
  areas_plantadas <- dados_csv$area_m2
  cat(sprintf("Dados lidos de '%s' (%d registro(s) cadastrados no Python).\n\n", arquivo_dados, nrow(dados_csv)))
} else {
  cat(sprintf("Aviso: '%s' não encontrado. Rode primeiro o programa em Python para gerar os dados.\n", arquivo_dados))
  cat("Usando dados de exemplo para não interromper a execução.\n\n")
  areas_plantadas <- c(1500, 2300, 1800, 3100, 2750)
}

media_area <- mean(areas_plantadas)
desvio_area <- sd(areas_plantadas)

cat(sprintf("Média da área: %.2f m²\n", media_area))
cat(sprintf("Desvio Padrão: %.2f m²\n\n", desvio_area))

cat("--- CLIMA ATUAL (PORTO ALEGRE) ---\n")
url <- "https://api.open-meteo.com/v1/forecast?latitude=-30.03&longitude=-51.23&current_weather=true"
resposta <- GET(url)
dados_clima <- fromJSON(rawToChar(resposta$content))
clima_atual <- dados_clima$current_weather
cat(sprintf("Temperatura: %s °C\n", clima_atual$temperature))
cat(sprintf("Velocidade do Vento: %s km/h\n", clima_atual$windspeed))
