"""
Global Solution 2025.2 - Future at Work
Disciplina: Pensamento Computacional e Automação com Python
Sistema de orientação de carreiras do futuro (CLI).

Para executar:
    python main.py
"""

from models.perfil import Perfil
from models.carreira import Carreira
from models.recomendador import Recomendador
from data.carreiras_exemplo import CARREIRAS_EXEMPLO


def criar_recomendador_padrao() -> Recomendador:
    carreiras = []
    for c in CARREIRAS_EXEMPLO:
        carreiras.append(
            Carreira(
                nome=c["nome"],
                descricao=c["descricao"],
                trilha_aprendizado=c["trilha_aprendizado"],
                competencias_relevantes=c["competencias_relevantes"],
                foco_futuro=c["foco_futuro"],
            )
        )
    return Recomendador(carreiras=carreiras)


def cadastrar_perfil() -> Perfil:
    print("\n=== Cadastro de Perfil Profissional do Futuro ===")
    nome = input("Nome completo: ").strip()
    rm = input("RM (opcional): ").strip()

    perfil = Perfil(nome=nome, rm=rm)

    print("\nAvalie suas competências de 0 a 10:")
    competencias_base = [
        ("logica_programacao", "Lógica e raciocínio lógico"),
        ("criatividade", "Criatividade e pensamento inovador"),
        ("colaboracao", "Colaboração e trabalho em equipe"),
        ("adaptabilidade", "Adaptabilidade a mudanças"),
        ("comunicacao", "Comunicação"),
        ("dados_analise", "Interesse em dados e análise"),
        ("ia_aprendizado", "Interesse em IA e aprendizado contínuo"),
    ]

    for chave, descricao in competencias_base:
        while True:
            try:
                valor = float(
                    input(f"{descricao} (0 a 10): ").replace(",", ".").strip() or "0"
                )
                if 0 <= valor <= 10:
                    perfil.competencias[chave] = valor
                    break
                else:
                    print("Digite um valor entre 0 e 10.")
            except ValueError:
                print("Valor inválido. Use números, ex: 7.5")

    print("\nPerfil cadastrado com sucesso!\n")
    return perfil


def exibir_menu():
    print("=" * 70)
    print("SISTEMA DE ORIENTAÇÃO DE CARREIRAS DO FUTURO - Future Skills Lab")
    print("=" * 70)
    print("1 - Cadastrar/atualizar perfil")
    print("2 - Listar carreiras do futuro disponíveis")
    print("3 - Gerar recomendações para o perfil atual")
    print("4 - Exportar resumo do perfil e recomendações para arquivo .txt")
    print("0 - Sair")


def listar_carreiras(recomendador: Recomendador):
    print("\n=== Carreiras do Futuro ===")
    for idx, carreira in enumerate(recomendador.carreiras, start=1):
        print(f"{idx}. {carreira.nome} - foco: {carreira.foco_futuro}")
    print()


def gerar_recomendacoes(perfil: Perfil, recomendador: Recomendador):
    if perfil is None:
        print("\nNenhum perfil cadastrado ainda. Cadastre um perfil primeiro.\n")
        return None

    print("\n=== Recomendações de carreira para:", perfil.nome, "===")
    resultados = recomendador.recomendar(perfil, limite=5)

    if not resultados:
        print("Não foi possível gerar recomendações. Verifique os dados do perfil.\n")
        return None

    for idx, item in enumerate(resultados, start=1):
        carreira = item["carreira"]
        score = item["score_normalizado"]
        gaps = item["competencias_a_desenvolver"]

        print(f"\n{idx}) {carreira.nome}  |  Aderência: {score:.1f}%")
        print("   Descrição:", carreira.descricao)
        print("   Trilha de aprendizado sugerida:")
        for passo in carreira.trilha_aprendizado:
            print("    -", passo)

        if gaps:
            print("   Competências a fortalecer para essa carreira:")
            for comp, valor in gaps.items():
                print(f"    - {comp}: ideal ~{valor:.1f}")
        else:
            print("   Você já tem um bom alinhamento com essa carreira!")

    print()
    return resultados


def exportar_resumo(perfil: Perfil, recomendador: Recomendador):
    if perfil is None:
        print("\nNenhum perfil cadastrado ainda. Cadastre um perfil primeiro.\n")
        return

    resultados = recomendador.recomendar(perfil, limite=3)
    if not resultados:
        print("Não há recomendações para exportar.\n")
        return

    nome_arquivo = "resumo_perfil_carreiras.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("Resumo de Perfil - Sistema de Orientação de Carreiras do Futuro\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Nome: {perfil.nome}\n")
        if perfil.rm:
            f.write(f"RM: {perfil.rm}\n")
        f.write("\nCompetências (0 a 10):\n")
        for k, v in perfil.competencias.items():
            f.write(f"- {k}: {v}\n")

        f.write("\nTop 3 recomendações:\n")
        for item in resultados:
            carreira = item["carreira"]
            score = item["score_normalizado"]
            f.write(f"\n- {carreira.nome} (aderência: {score:.1f}%)\n")
            f.write("  Trilha sugerida:\n")
            for passo in carreira.trilha_aprendizado:
                f.write(f"   * {passo}\n")

    print(f"\nResumo exportado para: {nome_arquivo}\n")


def main():
    recomendador = criar_recomendador_padrao()
    perfil_atual = None

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            perfil_atual = cadastrar_perfil()
        elif opcao == "2":
            listar_carreiras(recomendador)
        elif opcao == "3":
            gerar_recomendacoes(perfil_atual, recomendador)
        elif opcao == "4":
            exportar_resumo(perfil_atual, recomendador)
        elif opcao == "0":
            print("\nEncerrando o sistema. Obrigado por utilizar o Future Skills Lab!\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
