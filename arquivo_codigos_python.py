import csv

registros = []
ARQUIVO_DADOS = "dados_agro.csv"

def salvar_csv():
    with open(ARQUIVO_DADOS, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["cultura", "area_m2", "quantidade_insumo", "unidade_insumo"])
        for cultura, area, quantidade, unidade in registros:
            escritor.writerow([cultura, area, quantidade, unidade])

def calcular_area_soja():
    print("\n--- Cálculo de Área (Retângulo) ---")
    base = float(input("Digite a largura da área (m): "))
    altura = float(input("Digite o comprimento da área (m): "))
    return base * altura
def calcular_area_arroz():
    print("\n--- Cálculo de Área (Círculo - Pivô) ---")
    raio = float(input("Digite o raio do pivô (m): "))
    return 3.14159 * (raio ** 2)
def calcular_insumo_soja():
    print("\n--- Manejo: Herbicida ---")
    ruas = int(input("Quantas ruas a lavoura tem? "))
    comprimento = float(input("Qual o comprimento de cada rua (m)? "))
    return (ruas * comprimento * 0.5), "Litros de Herbicida"
def calcular_insumo_arroz():
    print("\n--- Manejo: Ureia ---")
    ruas = int(input("Quantas ruas a lavoura tem? "))
    comprimento = float(input("Qual o comprimento de cada rua (m)? "))
    return (ruas * comprimento * 0.2), "Kg de Ureia"
while True:
    print("\n==================================")
    print("   FARMTECH SOLUTIONS - MENU")
    print("==================================")
    print("1. Entrada de dados")
    print("2. Saída de dados (Relatório)")
    print("3. Atualização de dados")
    print("4. Deleção de dados")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\n[1] Soja  |  [2] Arroz")
        escolha = input("Escolha a cultura: ")
        if escolha == '1':
            registros.append(["Soja", calcular_area_soja(), *calcular_insumo_soja()])
            salvar_csv()
            print("=> Registro salvo com sucesso!")
        elif escolha == '2':
            registros.append(["Arroz", calcular_area_arroz(), *calcular_insumo_arroz()])
            salvar_csv()
            print("=> Registro salvo com sucesso!")

    elif opcao == '2':
        if not registros:
            print("=> Nenhum dado cadastrado.")
        else:
            for i, dado in enumerate(registros):
                print(f"Posição {i} | {dado[0]} | Área: {dado[1]:.2f}m² | Insumo: {dado[2]:.2f} {dado[3]}")

    elif opcao == '3':
        pos = int(input(f"Digite a posição (0 a {len(registros)-1}): "))
        if 0 <= pos < len(registros):
            escolha = input("Nova cultura: [1] Soja | [2] Arroz: ")
            if escolha == '1':
                registros[pos] = ["Soja", calcular_area_soja(), *calcular_insumo_soja()]
            elif escolha == '2':
                registros[pos] = ["Arroz", calcular_area_arroz(), *calcular_insumo_arroz()]
            salvar_csv()
            print("=> Atualizado!")

    elif opcao == '4':
        pos = int(input(f"Posição para APAGAR (0 a {len(registros)-1}): "))
        if 0 <= pos < len(registros):
            registros.pop(pos)
            salvar_csv()
            print("=> Deletado!")

    elif opcao == '5':
        print("Encerrando...")
        break
