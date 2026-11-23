import argparse
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(BASE_DIR / "top5_leagues_player.csv")
df["price_num"] = pd.to_numeric(df["price"], errors="coerce")
df["age_num"] = pd.to_numeric(df["age"], errors="coerce")

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

ORDEM_CHAVES_POSICAO = [
    "goalkeeper",
    "left_back",
    "right_back",
    "centre_back",
    "defensive_midfield",
    "central_midfield",
    "attacking_midfield",
    "left_winger",
    "right_winger",
    "centre_forward",
]

TEXTOS = {
    "pt": {
        "leagues_avail": "Ligas disponiveis",
        "filter_prompt": "Filtrar por liga (ou aperte Enter para ver todas): ",
        "not_found": "Liga nao encontrada. Mostrando todas as ligas.",
        "all_leagues": "TODAS AS LIGAS",
        "overview": "VISAO GERAL",
        "records": "Registros na selecao",
        "distinct_names": "Nomes distintos",
        "distinct_clubs": "Clubes distintos",
        "distinct_leagues": "Ligas distintas",
        "avg_age": "Idade media",
        "yrs": "anos",
        "avg_val": "Valor medio",
        "by_league": "RESUMO POR LIGA",
        "col_league": "Liga",
        "col_players": "Jog.",
        "col_age": "Idade",
        "col_avg_eur": "Valor Medio (€M)",
        "col_max_eur": "Maior (€M)",
        "by_pos": "JOGADORES POR POSICAO",
        "col_pos": "Posicao",
        "col_qty": "Jogadores",
        "top_val": "TOP 10 MAIORES VALORES DE MERCADO",
        "col_player": "Jogador",
        "col_club": "Clube",
        "col_val_eur": "Valor (€M)",
    },
    "en": {
        "leagues_avail": "Available leagues",
        "filter_prompt": "Filter by league (or press Enter for all): ",
        "not_found": "League not found. Showing all leagues.",
        "all_leagues": "ALL LEAGUES",
        "overview": "OVERVIEW",
        "records": "Records in selection",
        "distinct_names": "Distinct names",
        "distinct_clubs": "Distinct clubs",
        "distinct_leagues": "Distinct leagues",
        "avg_age": "Average age",
        "yrs": "yrs",
        "avg_val": "Average value",
        "by_league": "SUMMARY BY LEAGUE",
        "col_league": "League",
        "col_players": "Ply.",
        "col_age": "Age",
        "col_avg_eur": "Avg. Value (€M)",
        "col_max_eur": "Max (€M)",
        "by_pos": "PLAYERS BY POSITION",
        "col_pos": "Position",
        "col_qty": "Players",
        "top_val": "TOP 10 MARKET VALUES",
        "col_player": "Player",
        "col_club": "Club",
        "col_val_eur": "Value (€M)",
    },
}

L = 78


def linha(char="-"):
    print(char * L)


def titulo(texto):
    print("\n" + "=" * L)
    print(f"  {texto}")
    print("=" * L)


def moeda(val_eur):
    if pd.isna(val_eur):
        return "N/A"
    return (
        f"€ {val_eur:6.2f}M  |  "
        f"US$ {val_eur * EUR_PARA_USD:6.2f}M  |  "
        f"R$ {val_eur * EUR_PARA_BRL:6.2f}M"
    )


def mapear_chave_posicao(pos):
    if pd.isna(pos) or str(pos).strip() == "":
        return None
    chave = " ".join(str(pos).strip().lower().split())
    return MAPA_POSICOES_CANONICO.get(chave)


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

ligas_disponiveis = sorted(df["league"].dropna().astype(str).unique())

print("\n" + "-" * L)
print(f"{t['leagues_avail']}: " + ", ".join(ligas_disponiveis))
filtro_liga = input(t["filter_prompt"]).strip()

if filtro_liga:
    base = df[df["league"].astype(str).str.lower() == filtro_liga.lower()]
    if base.empty:
        base = df[df["league"].astype(str).str.contains(filtro_liga, case=False, na=False)]
    if base.empty:
        print(t["not_found"])
        base = df
        nome_escopo = t["all_leagues"]
    else:
        nome_escopo = str(base["league"].iloc[0])
else:
    base = df
    nome_escopo = t["all_leagues"]

titulo(f"{t['overview']} - {nome_escopo}")
print(f"  {t['records']:<22}: {len(base)}")
print(f"  {t['distinct_names']:<22}: {base['name'].nunique()}")
print(f"  {t['distinct_clubs']:<22}: {base['club'].nunique()}")
if nome_escopo == t["all_leagues"]:
    print(f"  {t['distinct_leagues']:<22}: {base['league'].nunique()}")
print(f"  {t['avg_age']:<22}: {base['age_num'].mean():.1f} {t['yrs']}")
print(f"  {t['avg_val']:<22}: {moeda(base['price_num'].mean())}")

if nome_escopo == t["all_leagues"]:
    titulo(t["by_league"])
    print(f"  {t['col_league']:<14} {t['col_players']:>5} {t['col_age']:>6} {t['col_avg_eur']:>17} {t['col_max_eur']:>12}")
    linha("-")

    agrupado = (
        base.groupby("league", dropna=False)
        .agg(
            jogadores=("name", "count"),
            idade=("age_num", "mean"),
            media_eur=("price_num", "mean"),
            max_eur=("price_num", "max"),
        )
        .sort_values("media_eur", ascending=False)
    )

    for liga_nome, row in agrupado.iterrows():
        liga_txt = str(liga_nome) if pd.notna(liga_nome) else "-"
        idade_txt = f"{row['idade']:.1f}" if pd.notna(row["idade"]) else "-"
        media_txt = f"€ {row['media_eur']:.2f}M" if pd.notna(row["media_eur"]) else "-"
        max_txt = f"€ {row['max_eur']:.2f}M" if pd.notna(row["max_eur"]) else "-"
        print(f"  {liga_txt:<14} {int(row['jogadores']):>5} {idade_txt:>6} {media_txt:>17} {max_txt:>12}")

titulo(f"{t['by_pos']} - {nome_escopo}")
chaves_pos = base["position"].apply(mapear_chave_posicao).dropna().value_counts()
print(f"  {t['col_pos']:<28} {t['col_qty']:>10}")
linha("-")
for chave_pos in ORDEM_CHAVES_POSICAO:
    nome_pos = NOMES_POSICOES[lang].get(chave_pos, chave_pos)
    qtd = int(chaves_pos.get(chave_pos, 0))
    print(f"  {nome_pos:<28} {qtd:>10}")

titulo(f"{t['top_val']} - {nome_escopo}")
col_liga_cab = f" {t['col_league']:<11}" if nome_escopo == t["all_leagues"] else ""
print(f"  {'#':>2}  {t['col_player']:<22} {t['col_club']:<20}{col_liga_cab} {t['col_age']:>5} {t['col_val_eur']:>11}")
linha("-")
top_val = base.sort_values("price_num", ascending=False).head(10)
for i, (_, r) in enumerate(top_val.iterrows(), start=1):
    nome = str(r.get("name", "-"))[:22]
    clube = str(r.get("club", "-"))[:20]
    liga_col = f" {str(r.get('league', '-'))[:11]:<11}" if nome_escopo == t["all_leagues"] else ""
    idade_r = f"{r['age_num']:.0f}" if pd.notna(r["age_num"]) else "-"
    valor_r = f"€ {r['price_num']:.2f}M" if pd.notna(r["price_num"]) else "-"
    print(f"  {i:>2}  {nome:<22} {clube:<20}{liga_col} {idade_r:>5} {valor_r:>11}")

print()