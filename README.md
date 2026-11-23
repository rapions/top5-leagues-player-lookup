# Top 5 Leagues Player Lookup (PT/EN)

Bilingual (PT/EN) terminal script using `top5_leagues_player.csv` (2,612 player records) to filter by league, search players, display basic profile fields (age, birthplace, club, position), and view market values in `€ M`, `US$ M` (`1.08`), and `R$ M` (`6.10`).

Script bilíngue (PT/EN) no terminal usando `top5_leagues_player.csv` (2.612 registros de jogadores) para filtrar por liga, buscar jogadores, exibir dados básicos (idade, local de nascimento, clube, posição) e consultar valores de mercado em `€ M`, `US$ M` (`1,08`) e `R$ M` (`6,10`).

---

## Files / Arquivos

- `menu.py` — Language selection (`1 - PT/BR`, `2 - EN`, `3 - Exit / Sair`) and main menu (`0` returns to language screen).
- `resumo_base.py` — League filter, position counts, and top market values.
- `buscar_jogador.py` — Player search by name and display of basic fields and market value.
- `top5_leagues_player.csv` — Player dataset.

---

## How to Run / Como Executar

### Windows shortcut (`.lnk`)
Open your shortcut pointing to `menu.py` with **Start in / Iniciar em** set to the project folder.

### Terminal
    py menu.py

---

## Notes / Observações

- Fixed conversion rates (`1.08` for `US$ M` and `6.10` for `R$ M`) and position labels are set directly in the scripts.
- Raw CSV fields (such as nationality, birthplace, or preferred foot) are shown as they appear in the file.