import argparse
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / "top5_leagues_player.csv")
df["price_num"] = pd.to_numeric(df["price"], errors="coerce")
df["max_price_num"] = pd.to_numeric(df["max_price"], errors="coerce")
df["age_num"] = pd.to_numeric(df["age"], errors="coerce")
df["height_num"] = pd.to_numeric(df["height"], errors="coerce")

EUR_PARA_USD = 1.08
EUR_PARA_BRL = 6.10

MAPA_POSICOES_CANONICO = {
    "goalkeeper": "goalkeeper",
    "keeper": "goalkeeper",
    "defender - centre-back": "centre_back",
    "centre-back": "centre_back",
    "center-back": "centre_back",
    "defender - right-back": "right_back",
    "right-back": "right_back",
    "defender - left-back": "left_back",
    "left-back": "left_back",
    "midfield - defensive midfield": "defensive_midfield",
    "defensive midfield": "defensive_midfield",
    "midfield - central midfield": "central_midfield",
    "central midfield": "central_midfield",
    "midfield - attacking midfield": "attacking_midfield",
    "attacking midfield": "attacking_midfield",
    "midfield - left midfield": "left_midfield",
    "left midfield": "left_midfield",
    "midfield - right midfield": "right_midfield",
    "right midfield": "right_midfield",
    "attack - centre-forward": "centre_forward",
    "centre-forward": "centre_forward",
    "center-forward": "centre_forward",
    "attack - second striker": "second_striker",
    "second striker": "second_striker",
    "attack - left winger": "left_winger",
    "left winger": "left_winger",
    "attack - right winger": "right_winger",
    "right winger": "right_winger",
}

NOMES_POSICOES = {
    "pt": {
        "goalkeeper": "Goleiro",
        "left_back": "Lateral Esquerdo",
        "right_back": "Lateral Direito",
        "centre_back": "Zagueiro",
        "defensive_midfield": "Volante",
        "central_midfield": "Meia Central",
        "attacking_midfield": "Meia Atacante",
        "left_winger": "Ponta Esquerda",
        "right_winger": "Ponta Direita",
        "centre_forward": "Centroavante",
        "second_striker": "Segundo Atacante",
        "left_midfield": "Meia Esquerda",
        "right_midfield": "Meia Direita",
    },
    "en": {
        "goalkeeper": "Goalkeeper",
        "left_back": "Left-Back",
        "right_back": "Right-Back",
        "centre_back": "Centre-Back",
        "defensive_midfield": "Defensive Midfield",
        "central_midfield": "Central Midfield",
        "attacking_midfield": "Attacking Midfield",
        "left_winger": "Left Winger",
        "right_winger": "Right Winger",
        "centre_forward": "Centre-Forward",
        "second_striker": "Second Striker",
        "left_midfield": "Left Midfield",
        "right_midfield": "Right Midfield",
    },
}

TEXTOS = {
    "pt": {
        "title": "BUSCAR JOGADOR",
        "prompt": "Digite o nome do jogador (ou 0 para voltar ao menu): ",
        "back": "Voltando ao menu...",
        "empty": "Digite pelo menos uma letra ou 0 para voltar.",
        "not_found": "Nenhum jogador encontrado com esse termo.",
        "matches": "Jogador(es) encontrado(s)",
        "full_name": "Nome completo",
        "age": "Idade",
        "yrs": "anos",
        "height": "Altura",
        "nationality": "Nacionalidade",
        "birthplace": "Local de nascimento",
        "position": "Posicao",
        "foot": "Pe preferido",
        "shirt": "Camisa",
        "club": "Clube",
        "league": "Liga",
        "joined": "Chegada ao clube",
        "contract": "Fim do contrato",
        "agent": "Empresario",
        "outfitter": "Fornecedor",
        "market_val": "Valor de mercado",
        "peak_val": "Maior valor historico",
        "na": "N/A",
    },
    "en": {
        "title": "SEARCH PLAYER",
        "prompt": "Enter player name (or 0 to return to menu): ",
        "back": "Returning to menu...",
        "empty": "Type at least one character or 0 to return.",
        "not_found": "No player found matching this query.",
        "matches": "Player(s) found",
        "full_name": "Full name",
        "age": "Age",
        "yrs": "yrs",
        "height": "Height",
        "nationality": "Nationality",
        "birthplace": "Place of birth",
        "position": "Position",
        "foot": "Preferred foot",
        "shirt": "Shirt number",
        "club": "Club",
        "league": "League",
        "joined": "Joined club",
        "contract": "Contract expires",
        "agent": "Agent",
        "outfitter": "Outfitter",
        "market_val": "Market value",
        "peak_val": "Peak market value",
        "na": "N/A",
    },
}

L = 78


def linha(char="-"):
    print(char * L)


def titulo(texto):
    print("\n" + "=" * L)
    print(f"  {texto}")
    print("=" * L)


def formatar_moeda(val_eur, na_txt):
    if pd.isna(val_eur):
        return na_txt
    return (
        f"€ {val_eur:6.2f}M  |  "
        f"US$ {val_eur * EUR_PARA_USD:6.2f}M  |  "
        f"R$ {val_eur * EUR_PARA_BRL:6.2f}M"
    )


def formatar_posicao(pos, lang, na_txt):
    if pd.isna(pos) or str(pos).strip() == "":
        return na_txt
    limpo = " ".join(str(pos).strip().split())
    chave = MAPA_POSICOES_CANONICO.get(limpo.lower())
    if chave and chave in NOMES_POSICOES[lang]:
        return NOMES_POSICOES[lang][chave]
    return limpo


def campo_texto(row, col, na_txt):
    if col not in row or pd.isna(row[col]) or str(row[col]).strip() == "":
        return na_txt
    return str(row[col]).strip()


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("--lang", choices=["pt", "en"], default=None)
args, _ = parser.parse_known_args()

if args.lang:
    lang = args.lang
else:
    print("\n1 - PT/BR\n2 - EN")
    escolha_lang = input("Idioma / Language [1/2] (Enter = 1): ").strip()
    lang = "en" if escolha_lang == "2" else "pt"

t = TEXTOS[lang]

while True:
    titulo(t["title"])
    termo = input(t["prompt"]).strip()

    if termo in ("0", "sair", "voltar", "exit", "back"):
        print(t["back"])
        break

    if not termo:
        print(t["empty"])
        continue

    mask_nome = df["name"].astype(str).str.contains(termo, case=False, na=False)
    mask_completo = (
        df["full_name"].astype(str).str.contains(termo, case=False, na=False)
        if "full_name" in df.columns
        else pd.Series(False, index=df.index)
    )
    achados = df[mask_nome | mask_completo]

    if achados.empty:
        print(t["not_found"])
        continue

    print(f"\n{t['matches']}: {len(achados)}")
    for _, r in achados.head(10).iterrows():
        linha("-")
        nome = campo_texto(r, "name", t["na"])
        print(f"  {nome}")
        print(f"  {t['full_name']:<22}: {campo_texto(r, 'full_name', t['na'])}")

        idade_txt = f"{r['age_num']:.0f} {t['yrs']}" if pd.notna(r["age_num"]) else t["na"]
        altura_txt = f"{r['height_num']:.2f} m" if pd.notna(r["height_num"]) else campo_texto(r, "height", t["na"])

        print(f"  {t['age']:<22}: {idade_txt}")
        print(f"  {t['height']:<22}: {altura_txt}")
        print(f"  {t['nationality']:<22}: {campo_texto(r, 'nationality', t['na'])}")
        print(f"  {t['birthplace']:<22}: {campo_texto(r, 'place_of_birth', t['na'])}")
        print(f"  {t['position']:<22}: {formatar_posicao(r.get('position'), lang, t['na'])}")
        print(f"  {t['foot']:<22}: {campo_texto(r, 'foot', t['na'])}")
        print(f"  {t['shirt']:<22}: {campo_texto(r, 'shirt_nr', t['na'])}")
        print(f"  {t['club']:<22}: {campo_texto(r, 'club', t['na'])}")
        print(f"  {t['league']:<22}: {campo_texto(r, 'league', t['na'])}")
        print(f"  {t['joined']:<22}: {campo_texto(r, 'joined_club', t['na'])}")
        print(f"  {t['contract']:<22}: {campo_texto(r, 'contract_expires', t['na'])}")
        print(f"  {t['agent']:<22}: {campo_texto(r, 'player_agent', t['na'])}")
        print(f"  {t['outfitter']:<22}: {campo_texto(r, 'outfitter', t['na'])}")
        print(f"  {t['market_val']:<22}: {formatar_moeda(r['price_num'], t['na'])}")
        print(f"  {t['peak_val']:<22}: {formatar_moeda(r['max_price_num'], t['na'])}")
    linha("-")