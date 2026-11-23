from pathlib import Path
import subprocess
import sys

BASE_DIR = Path(__file__).resolve().parent

TEXTOS = {
    "pt": {
        "menu_title": "ANALISE DE DADOS - TOP 5 LIGAS",
        "opt_1": "[1] Resumo geral, ligas, posicoes e top valores",
        "opt_2": "[2] Buscar jogador especifico",
        "opt_0": "[0] Voltar para selecao de idioma",
        "menu_prompt": "Escolha uma opcao: ",
        "invalid": "Opcao invalida. Tente novamente.",
        "back_lang": "Voltando para selecao de idioma...",
        "missing": "Arquivo nao encontrado na pasta do projeto",
    },
    "en": {
        "menu_title": "TOP 5 LEAGUES PLAYER DATA ANALYSIS",
        "opt_1": "[1] Overview, leagues, positions and top market values",
        "opt_2": "[2] Search specific player",
        "opt_0": "[0] Back to language selection",
        "menu_prompt": "Choose an option: ",
        "invalid": "Invalid option. Try again.",
        "back_lang": "Returning to language selection...",
        "missing": "File not found in project folder",
    },
}


def tela_idioma():
    while True:
        print("\n" + "=" * 50)
        print("  1 - PT/BR")
        print("  2 - EN")
        print("  3 - Sair")
        print("=" * 50)
        escolha = input("Escolha / Choose [1/2/3]: ").strip()

        if escolha == "1":
            return "pt"
        if escolha == "2":
            return "en"
        if escolha == "3":
            print("Saindo / Exiting...")
            return None
        print("Opcao invalida / Invalid option. Digite 1, 2 ou 3.")


def rodar_script(nome_arquivo, lang):
    caminho = BASE_DIR / nome_arquivo
    if not caminho.exists():
        print(f"{TEXTOS[lang]['missing']}: {caminho}")
        return
    print()
    subprocess.run(
        [sys.executable, str(caminho), "--lang", lang],
        cwd=str(BASE_DIR),
        check=False,
    )


while True:
    lang = tela_idioma()
    if lang is None:
        break

    while True:
        t = TEXTOS[lang]
        print("\n" + "=" * 50)
        print(f"  {t['menu_title']} ({'PT/BR' if lang == 'pt' else 'EN'})")
        print("=" * 50)
        print(f"  {t['opt_1']}")
        print(f"  {t['opt_2']}")
        print(f"  {t['opt_0']}")
        print("-" * 50)

        opcao = input(t["menu_prompt"]).strip()

        if opcao == "1":
            rodar_script("resumo_base.py", lang)
        elif opcao == "2":
            rodar_script("buscar_jogador.py", lang)
        elif opcao == "0":
            print(t["back_lang"])
            break
        else:
            print(t["invalid"])