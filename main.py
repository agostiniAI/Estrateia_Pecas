def cadastrar_peca(pecas):
    """Pede os dados de uma peça, avalia e adiciona na lista de peças."""
    id_peca = int(input("ID da peça: "))
    peso = float(input("Peso (g): "))
    cor = input("Cor: ").strip().lower()
    comprimento = float(input("Comprimento (cm): "))

    motivos = []

    if peso < 95 or peso > 105:
        motivos.append("peso fora do padrão (95-105g)")

    if cor not in ["azul", "verde"]:
        motivos.append("cor não permitida (deve ser azul ou verde)")

    if comprimento < 10 or comprimento > 20:
        motivos.append("comprimento fora do padrão (10-20cm)")

    if motivos:
        status = "reprovada"
        motivo_final = ", ".join(motivos)
    else:
        status = "aprovada"
        motivo_final = None

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status,
        "motivo": motivo_final,
    }

    pecas.append(peca)
    print(f"Peça {id_peca} cadastrada como {status}.")
    return peca


def adicionar_a_caixa(peca, caixa_atual, caixas_fechadas):
    """Adiciona uma peça aprovada à caixa atual; fecha e abre nova caixa se necessário."""
    if peca["status"] != "aprovada":
        return caixa_atual

    caixa_atual.append(peca)

    if len(caixa_atual) == 10:
        caixas_fechadas.append(caixa_atual)
        caixa_atual = []

    return caixa_atual


def listar_pecas(pecas, filtro=None):
    """Lista peças cadastradas. filtro pode ser 'aprovada', 'reprovada' ou None (lista todas)."""
    encontrou = False
    for peca in pecas:
        if filtro is None or peca["status"] == filtro:
            print("ID:", peca["id"], "| Peso:", peca["peso"], "g | Cor:", peca["cor"], "| Comprimento:", peca["comprimento"], "cm | Status:", peca["status"], "| Motivo:", peca["motivo"])
            encontrou = True

    if not encontrou:
        print("Nenhuma peça encontrada.")


def remover_peca(pecas, id_peca):
    """Remove a peça com o id informado da lista de peças cadastradas."""
    for peca in pecas:
        if peca["id"] == id_peca:
            pecas.remove(peca)
            print(f"Peça {id_peca} removida com sucesso.")
            return True

    print(f"Peça {id_peca} não encontrada.")
    return False


def listar_caixas_fechadas(caixas_fechadas):
    """Lista as caixas fechadas com sua numeração."""
    if not caixas_fechadas:
        print("Nenhuma caixa fechada ainda.")
        return

    for numero_caixa, caixa in enumerate(caixas_fechadas, start=1):
        print(f"Caixa {numero_caixa}: {caixa}")


def gerar_relatorio(pecas, caixa_atual, caixas_fechadas):
    """Imprime um relatório consolidado do sistema."""
    total_aprovadas = 0
    total_reprovadas = 0
    detalhes_reprovadas = []

    for peca in pecas:
        if peca["status"] == "aprovada":
            total_aprovadas += 1
        else:
            total_reprovadas += 1
            detalhes_reprovadas.append(
                f"ID {peca['id']}: {peca['motivo']}"
            )

    print("\n===== RELATÓRIO FINAL =====")
    print("Total de peças aprovadas:", total_aprovadas)
    print("Total de peças reprovadas:", total_reprovadas)

    if detalhes_reprovadas:
        print("Motivos das reprovações:")
        for linha in detalhes_reprovadas:
            print(" -", linha)

    total_caixas = len(caixas_fechadas) + (1 if caixa_atual else 0)
    print("Quantidade de caixas utilizadas:", total_caixas)


def exibir_menu():
    print("\n===== MENU =====")
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("6. Sair")


def main():
    pecas = []
    caixa_atual = []
    caixas_fechadas = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            peca = cadastrar_peca(pecas)
            caixa_atual = adicionar_a_caixa(peca, caixa_atual, caixas_fechadas)

        elif opcao == "2":
            sub = input("Ver (a)provadas, (r)eprovadas ou (t)odas? ").strip().lower()
            if sub == "a":
                listar_pecas(pecas, "aprovada")
            elif sub == "r":
                listar_pecas(pecas, "reprovada")
            else:
                listar_pecas(pecas)

        elif opcao == "3":
            id_remover = int(input("Digite o ID da peça a remover: "))
            remover_peca(pecas, id_remover)

        elif opcao == "4":
            listar_caixas_fechadas(caixas_fechadas)

        elif opcao == "5":
            gerar_relatorio(pecas, caixa_atual, caixas_fechadas)

        elif opcao == "6":
            print("Encerrando o programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
