# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.21.1",
#     "pandas==3.0.1",
#     "plotly==6.6.0",
# ]
# ///

import marimo

__generated_with = "0.20.1"
app = marimo.App(width="medium")


@app.cell
def imports():
    import marimo as mo
    import pandas as pd
    import plotly.express as px

    return mo, pd


@app.cell
def titel(mo):
    mo.md("""
    # Titel: [TITEL HIER EINFÜGEN]

    **Name:** [Ihr Name]

    **Datensatz:** [Name des Datensatzes + Link zur Quelle]

    **Ziel:** [Was können Nutzer:innen mit Ihrem Notebook visualisieren?]
    """)
    return


@app.cell
def daten_laden(mo, pd):
    # URL zum Datensatz (CSV) — passen Sie die URL an ihren Datensatz an
    url = "https://data.stadt-zuerich.ch/dataset/..."

    df = pd.read_csv(url)

    mo.md(
        f"""
        ## 1. Daten laden und erkunden

        Der Datensatz hat **{df.shape[0]:,} Zeilen** und **{df.shape[1]} Spalten**.

        Spalten: `{list(df.columns)}`
        """
    )
    return (df,)


@app.cell
def erste_zeilen(df):
    df.head(10)
    return


@app.cell
def beschreibung(mo):
    mo.md("""
    ### Was bedeuten die Spalten?

    | Spalte | Bedeutung |
    |--------|-----------|
    | `...` | ... |
    | `...` | ... |
    | `...` | ... |

    > Beschreiben Sie kurz, was die wichtigsten Spalten bedeuten.
    """)
    return


@app.cell
def grundstatistik(df):
    df.describe()
    return


@app.cell
def section_visualisierung1(mo):
    mo.md("""
    ---
    ## 2. Erste Visualisierung

    > Beschreiben Sie hier, was Sie zeigen wollen und warum Sie diesen Diagrammtyp gewählt haben.
    """)
    return


@app.cell
def visualisierung1():
    # === IHR CODE HIER ===
    # Beispiel Liniendiagramm:
    # fig = px.line(df, x="...", y="...", title="...")

    # Beispiel Balkendiagramm:
    # fig = px.bar(df, x="...", y="...", title="...")

    # fig
    pass
    return


@app.cell
def erklaerung1(mo):
    mo.md("""
    ### Was sehen wir?

    > Beschreiben Sie, was im Diagramm zu sehen ist.
    > Was fällt auf? Gibt es Trends, Ausreisser, Muster?
    """)
    return


@app.cell
def section_visualisierung2(mo):
    mo.md("""
    ---
    ## 3. Zweite Visualisierung

    > Beschreiben Sie ihre zweite Frage an die Daten.
    """)
    return


@app.cell
def visualisierung2():
    # === IHR CODE HIER ===
    pass
    return


@app.cell
def erklaerung2(mo):
    mo.md("""
    ### Was sehen sie?

    > Beschreiben Sie ihre Beobachtungen.
    """)
    return


@app.cell(hide_code=True)
def section_interaktiv(mo):
    mo.md("""
    ---
    ## 4. Interaktive Visualisierung

    > Fügen Sie ein UI-Element (Slider, Dropdown, Textfeld) ein,
    > damit man die Visualisierung interaktiv erkunden kann.
    """)
    return


@app.cell
def interaktiv_ui():
    # === UI-ELEMENT HIER ERSTELLEN ===
    # Beispiele:
    # slider = mo.ui.slider(start=2010, stop=2024, value=2020, label="Jahr:")
    # dropdown = mo.ui.dropdown(options=["A", "B", "C"], value="A", label="Wähle:")
    # text = mo.ui.text(value="Zürich", label="Eingabe:")

    # slider  # oder dropdown, text, etc.
    pass
    return


@app.cell
def interaktiv_plot():
    # === IHR CODE HIER ===
    # Hier greifen Sie auf den Wert des UI-Elements zu:
    # wert = slider.value  (oder dropdown.value, text.value)
    # Dann filtern Sie die Daten und erstellen den Plot.

    # Wichtig: mo.stop() verwenden falls keine Daten gefunden!
    # mo.stop(len(gefiltert) == 0, mo.md("Keine Daten gefunden."))
    pass
    return


if __name__ == "__main__":
    app.run()
