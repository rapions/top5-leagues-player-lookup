# Top 5 Leagues Player Lookup (PT/EN)

## Português (PT-BR)

Script bilíngue (PT/EN) no terminal usando `top5_leagues_player.csv` (2.612 registros de jogadores) para filtrar por liga, buscar jogadores, exibir dados básicos (idade, local de nascimento, clube, posição) e consultar valores de mercado em `€ M`, `US$ M` (`1,08`) e `R$ M` (`6,10`).

### Arquivos
- `menu.py` — Seleção de idioma (`1 - PT/BR`, `2 - EN`, `3 - Exit / Sair`) e menu principal (`0` retorna para a tela de idioma).
- `resumo_base.py` — Filtro por liga, contagem por posição e ranking dos maiores valores de mercado.
- `buscar_jogador.py` — Busca de jogadores por nome e exibição de dados cadastrais e valor de mercado.
- `top5_leagues_player.csv` — Base de dados dos jogadores.

### Como Executar
- Atalho no Windows (`.lnk`): Abra o atalho apontando para `menu.py` com o campo **Iniciar em** definido para a pasta do projeto.
- Terminal: `py menu.py`

### Observações
- As taxas de conversão (`1,08` para `US$ M` e `6,10` para `R$ M`) e os nomes das posições estão definidos diretamente nos scripts.
- Campos crus do CSV (como nacionalidade, local de nascimento ou pé preferido) são exibidos exatamente como constam no arquivo original.

---

## English (EN)

Bilingual (PT/EN) terminal script using `top5_leagues_player.csv` (2,612 player records) to filter by league, search players, display basic profile fields (age, birthplace, club, position), and view market values in `€ M`, `US$ M` (`1.08`), and `R$ M` (`6.10`).

### Files
- `menu.py` — Language selection (`1 - PT/BR`, `2 - EN`, `3 - Exit / Sair`) and main menu (`0` returns to the language screen).
- `resumo_base.py` — League filter, position counts, and top market values.
- `buscar_jogador.py` — Player search by name and display of basic fields and market value.
- `top5_leagues_player.csv` — Player dataset.

### How to Run
- Windows shortcut (`.lnk`): Open your shortcut pointing to `menu.py` with **Start in** set to the project folder.
- Terminal: `py menu.py`

### Notes
- Fixed conversion rates (`1.08` for `US$ M` and `6.10` for `R$ M`) and position labels are set directly in the scripts.
- Raw CSV fields (such as nationality, birthplace, or preferred foot) are shown as they appear in the file.
