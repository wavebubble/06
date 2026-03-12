import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def imports():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    return mo, pd, px


@app.cell
def einleitung(mo):
    mo.md(
        """
        # Datenvisualisierung mit Zürcher Open Data

        In diesem Notebook lernen wir, wie man mit Python Daten laden, erkunden und
        visualisieren kann. Als Datenquelle verwenden wir den **Vornamen-Datensatz**
        der Stadt Zürich — frei verfügbar auf
        [data.stadt-zuerich.ch](https://data.stadt-zuerich.ch/dataset/bev_bestand_vornamen_jahrgang_geschlecht_od3701).

        Der Datensatz enthält die Anzahl Personen der Wohnbevölkerung der Stadt Zürich
        nach Vorname, Geschlecht und Jahrgang.

        **Lernziele:**

        - CSV-Daten mit `pandas` laden und erkunden
        - Daten filtern und gruppieren
        - Linien- und Balkendiagramme mit `plotly` erstellen
        - Diagramme sinnvoll beschriften und gestalten
        """
    )
    return


@app.cell
def daten_laden(mo, pd):
    url = "https://data.stadt-zuerich.ch/dataset/bev_bestand_vornamen_jahrgang_geschlecht_od3701/download/BEV370OD3701.csv"

    df = pd.read_csv(url)

    mo.md(
        f"""
        ## 1. Daten laden und erkunden

        Wir laden die Daten direkt von der Website der Stadt Zürich:

        ```python
        import pandas as pd

        url = "https://data.stadt-zuerich.ch/dataset/bev_bestand_vornamen_jahrgang_geschlecht_od3701/download/BEV370OD3701.csv"
        df = pd.read_csv(url)
        ```

        Der Datensatz hat **{df.shape[0]:,} Zeilen** und **{df.shape[1]} Spalten**.

        Die Spalten heissen: `{list(df.columns)}`
        """
    )
    return df,


@app.cell
def head_anzeige(df):
    df.head(10)
    return


@app.cell
def spalten_erklaerung(mo):
    mo.md(
        """
        ### Was bedeuten die Spalten?

        | Spalte | Bedeutung |
        |--------|-----------|
        | `Vorname` | Der Vorname |
        | `Jahrgang` | Geburtsjahr |
        | `SexLang` | Geschlecht (`weiblich` / `männlich`) |
        | `AnzBestWir` | Anzahl Personen mit diesem Namen, Jahrgang und Geschlecht |

        > **Hinweis:** Es sind nur Vornamen enthalten, die mindestens 10 Mal pro Geschlecht
        > vorkommen. Seltene Namen fehlen also.
        """
    )
    return


@app.cell
def describe_anzeige(df):
    df.describe()
    return


@app.cell
def ueberblick_fragen(df, mo):
    anzahl_namen = df["Vorname"].nunique()
    min_jahr = df["Jahrgang"].min()
    max_jahr = df["Jahrgang"].max()

    mo.md(
        f"""
        ### Schnelle Fragen an die Daten

        Mit einfachen Pandas-Befehlen können wir erste Fragen beantworten:

        - **Wie viele verschiedene Vornamen** gibt es? → `df["Vorname"].nunique()` → **{anzahl_namen:,}**
        - **Welcher Zeitraum** wird abgedeckt? → `df["Jahrgang"].min()` / `.max()` → **{min_jahr}** bis **{max_jahr}**
        """
    )
    return


@app.cell
def section_filtern(mo):
    mo.md(
        """
        ---
        ## 2. Daten filtern

        Oft interessiert uns nicht der ganze Datensatz, sondern nur ein Teil davon.
        In Pandas filtern wir mit **Bedingungen in eckigen Klammern**.
        """
    )
    return


@app.cell
def filter_beispiel(df, mo):
    anna = df[df["Vorname"] == "Anna"]

    mo.md(
        f"""
        ### Beispiel: Alle Einträge für "Anna"

        ```python
        anna = df[df["Vorname"] == "Anna"]
        ```

        Das ergibt **{len(anna)} Zeilen** — eine pro Kombination aus Jahrgang und Geschlecht.
        """
    )
    return anna,


@app.cell
def anna_head(anna):
    anna.head(10)
    return


@app.cell
def filter_kombiniert(df, mo):
    mo.md(
        f"""
        ### Mehrere Filter kombinieren

        Wir können Bedingungen mit `&` (und) und `|` (oder) verknüpfen.
        **Wichtig:** Jede Bedingung muss in Klammern stehen!

        ```python
        anna_w = df[(df["Vorname"] == "Anna") & (df["SexLang"] == "weiblich")]
        ```

        Ergebnis: **{len(df[(df["Vorname"] == "Anna") & (df["SexLang"] == "weiblich")])} Zeilen** — nur weibliche Annas, eine pro Jahrgang.
        """
    )
    return


@app.cell
def section_liniendiagramm(mo):
    mo.md(
        """
        ---
        ## 3. Erstes Diagramm: Liniendiagramm

        Jetzt wird es visuell! Wir verwenden **Plotly Express** — eine Bibliothek,
        die mit wenig Code interaktive Diagramme erzeugt.

        **Frage:** Wie hat sich die Anzahl Personen mit dem Namen "Anna" über die
        Jahrgänge entwickelt?
        """
    )
    return


@app.cell
def liniendiagramm_anna(df, px):
    anna_plot = df[(df["Vorname"] == "Anna") & (df["SexLang"] == "weiblich")]

    fig_anna = px.line(
        anna_plot,
        x="Jahrgang",
        y="AnzBestWir",
        title="Anzahl Personen mit dem Vornamen Anna in Zürich",
        labels={"Jahrgang": "Geburtsjahr", "AnzBestWir": "Anzahl Personen"},
    )

    fig_anna
    return


@app.cell
def liniendiagramm_erklaerung(mo):
    mo.md(
        """
        ### Was sehen wir?

        - Die **x-Achse** zeigt den Jahrgang (Geburtsjahr)
        - Die **y-Achse** zeigt, wie viele Personen mit dem Namen Anna in Zürich wohnhaft sind
        - Bewege die Maus über die Linie, um genaue Werte zu sehen (Plotly ist interaktiv!)

        ### Der Code Schritt für Schritt

        ```python
        import plotly.express as px

        anna_w = df[(df["Vorname"] == "Anna") & (df["SexLang"] == "weiblich")]

        fig = px.line(
            anna_w,                          # Welche Daten?
            x="Jahrgang",                    # Was auf die x-Achse?
            y="AnzBestWir",                  # Was auf die y-Achse?
            title="Anzahl Personen ...",      # Titel des Diagramms
            labels={...},                    # Achsenbeschriftungen anpassen
        )
        fig  # Diagramm anzeigen
        ```
        """
    )
    return


@app.cell
def section_interaktiv(mo):
    mo.md(
        """
        ---
        ## 4. Interaktiv: Wähle deinen eigenen Namen

        Mit Marimo können wir ein Eingabefeld erstellen, damit du selbst einen Namen
        ausprobieren kannst.
        """
    )
    return


@app.cell
def name_ui(mo):
    name_input = mo.ui.text(
        value="Anna",
        label="Vorname eingeben:",
        full_width=False,
    )
    name_input
    return name_input,


@app.cell
def interaktiver_plot(df, mo, name_input, px):
    gewaehlter_name = name_input.value.strip()
    daten_name = df[df["Vorname"] == gewaehlter_name]

    mo.stop(
        len(daten_name) == 0,
        mo.md(
            f"""
            **Name "{gewaehlter_name}" nicht gefunden.**
            Nur Namen mit mindestens 10 Personen pro Geschlecht sind im Datensatz enthalten.
            Versuche es mit einem anderen Namen.
            """
        ),
    )

    fig_name = px.line(
        daten_name,
        x="Jahrgang",
        y="AnzBestWir",
        color="SexLang",
        title=f'Vorname "{gewaehlter_name}" in Zürich nach Jahrgang',
        labels={
            "Jahrgang": "Geburtsjahr",
            "AnzBestWir": "Anzahl Personen",
            "SexLang": "Geschlecht",
        },
        color_discrete_map={"weiblich": "#e74c8b", "männlich": "#3a86ff"},
    )
    fig_name.update_layout(legend_title_text="Geschlecht")
    fig_name
    return


@app.cell
def section_balkendiagramm(mo):
    mo.md(
        """
        ---
        ## 5. Balkendiagramm: Die beliebtesten Namen

        **Frage:** Was waren die häufigsten Vornamen für einen bestimmten Jahrgang?

        Dafür müssen wir:
        1. Nach Jahrgang und Geschlecht filtern
        2. Nach Anzahl sortieren
        3. Die Top 10 auswählen
        """
    )
    return


@app.cell
def balken_ui(mo):
    jahrgang_slider = mo.ui.slider(
        start=1940,
        stop=2024,
        value=2000,
        step=1,
        label="Jahrgang wählen:",
        show_value=True,
    )

    geschlecht_toggle = mo.ui.dropdown(
        options=["weiblich", "männlich"],
        value="weiblich",
        label="Geschlecht:",
    )

    mo.hstack([jahrgang_slider, geschlecht_toggle], gap=2)
    return geschlecht_toggle, jahrgang_slider


@app.cell
def top_namen_plot(df, geschlecht_toggle, jahrgang_slider, px):
    jahr = jahrgang_slider.value
    geschl = geschlecht_toggle.value

    top = (
        df[(df["Jahrgang"] == jahr) & (df["SexLang"] == geschl)]
        .sort_values("AnzBestWir", ascending=False)
        .head(10)
    )

    fig_top = px.bar(
        top,
        x="Vorname",
        y="AnzBestWir",
        title=f"Top 10 {geschl}e Vornamen — Jahrgang {jahr}",
        labels={"Vorname": "Vorname", "AnzBestWir": "Anzahl Personen"},
        color="AnzBestWir",
        color_continuous_scale="Viridis",
    )
    fig_top.update_layout(xaxis_tickangle=-45, showlegend=False)
    fig_top
    return


@app.cell
def section_vergleich(mo):
    mo.md(
        """
        ---
        ## 6. Mehrere Namen vergleichen

        Wir können auch mehrere Namen im selben Diagramm zeigen.
        So sieht man Trends und kann Namen miteinander vergleichen.
        """
    )
    return


@app.cell
def vergleich_ui(mo):
    namen_text = mo.ui.text(
        value="Anna, Lena, Emma, Sophie",
        label="Namen zum Vergleichen (kommagetrennt):",
        full_width=True,
    )

    geschlecht_vergleich = mo.ui.dropdown(
        options=["weiblich", "männlich"],
        value="weiblich",
        label="Geschlecht:",
    )

    mo.hstack([namen_text, geschlecht_vergleich], gap=2)
    return geschlecht_vergleich, namen_text


@app.cell
def vergleich_plot(df, geschlecht_vergleich, mo, namen_text, px):
    namen_liste = [n.strip() for n in namen_text.value.split(",") if n.strip()]

    vergleich = df[
        (df["Vorname"].isin(namen_liste))
        & (df["SexLang"] == geschlecht_vergleich.value)
    ]

    mo.stop(
        len(vergleich) == 0,
        mo.md("Keine Daten gefunden. Überprüfe die Schreibweise der Namen."),
    )

    fig_vergleich = px.line(
        vergleich,
        x="Jahrgang",
        y="AnzBestWir",
        color="Vorname",
        title="Vergleich: Vornamen in Zürich über die Zeit",
        labels={
            "Jahrgang": "Geburtsjahr",
            "AnzBestWir": "Anzahl Personen",
            "Vorname": "Vorname",
        },
    )
    fig_vergleich
    return


@app.cell
def section_gestaltung(mo):
    mo.md(
        """
        ---
        ## 7. Diagramme gestalten

        Gute Visualisierungen sind nicht nur korrekt, sondern auch **verständlich**.
        Hier ein paar Tipps:

        | Element | Warum wichtig? | Plotly-Parameter |
        |---------|---------------|-----------------|
        | **Titel** | Sagt, was das Diagramm zeigt | `title="..."` |
        | **Achsenbeschriftung** | Erklärt die Achsen | `labels={...}` |
        | **Legende** | Unterscheidet Kategorien | automatisch bei `color=` |
        | **Farben** | Lenken den Blick | `color_discrete_map=` oder `color_continuous_scale=` |

        ### Beispiel: Ein aufgehübschtes Diagramm
        """
    )
    return


@app.cell
def gestaltetes_diagramm(df, px):
    namen_maennl = ["Peter", "Thomas", "Michael", "Daniel", "Lukas", "Noah", "Liam"]
    daten_maennl = df[
        (df["Vorname"].isin(namen_maennl)) & (df["SexLang"] == "männlich")
    ]

    fig_gestaltet = px.line(
        daten_maennl,
        x="Jahrgang",
        y="AnzBestWir",
        color="Vorname",
        title="Männliche Vornamen im Wandel der Zeit — Stadt Zürich",
        labels={
            "Jahrgang": "Geburtsjahr",
            "AnzBestWir": "Anzahl Personen",
            "Vorname": "Vorname",
        },
    )

    fig_gestaltet.update_layout(
        font_family="Arial",
        title_font_size=18,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        legend_title_text="Vorname",
        hovermode="x unified",
        template="plotly_white",
    )

    fig_gestaltet
    return


@app.cell
def section_aufgaben(mo):
    mo.md(
        """
        ---
        ## 8. Aufgaben

        Jetzt bist du dran! Erstelle in den Zellen unten eigene Visualisierungen.

        ### Aufgabe 1: Dein Name
        Erstelle ein Liniendiagramm für deinen eigenen Vornamen.
        Falls dein Name nicht im Datensatz ist, wähle einen anderen.

        ### Aufgabe 2: Top-Namen deines Jahrgangs
        Erstelle ein Balkendiagramm mit den 10 häufigsten Namen deines Geburtsjahrgangs
        (für dein Geschlecht).

        ### Aufgabe 3: Vergleich
        Wähle 3–5 Namen und vergleiche sie in einem Liniendiagramm.
        Beschreibe in einem kurzen Text (als Kommentar im Code), welche Trends du siehst.

        ### Aufgabe 4 (Zusatz): Eigene Fragestellung
        Formuliere eine eigene Frage an die Daten und beantworte sie mit einer
        Visualisierung. Beispiele:
        - Welcher Name war in den 1970ern am beliebtesten und ist heute verschwunden?
        - Gibt es Namen, die sowohl bei Frauen als auch Männern vorkommen?
        - Wie hat sich die Vielfalt der Namen über die Zeit verändert?
        """
    )
    return


@app.cell
def aufgabe1_platz(mo):
    mo.md("### Dein Code für Aufgabe 1:")
    return


@app.cell
def aufgabe1():
    # Dein Code hier
    pass
    return


@app.cell
def aufgabe2_platz(mo):
    mo.md("### Dein Code für Aufgabe 2:")
    return


@app.cell
def aufgabe2():
    # Dein Code hier
    pass
    return


@app.cell
def aufgabe3_platz(mo):
    mo.md("### Dein Code für Aufgabe 3:")
    return


@app.cell
def aufgabe3():
    # Dein Code hier
    pass
    return


@app.cell
def aufgabe4_platz(mo):
    mo.md("### Dein Code für Aufgabe 4 (Zusatz):")
    return


@app.cell
def aufgabe4():
    # Dein Code hier
    pass
    return


@app.cell
def section_zusammenfassung(mo):
    mo.md(
        """
        ---
        ## Zusammenfassung

        Was wir gelernt haben:

        | Thema | Wichtigste Befehle |
        |-------|-------------------|
        | **Daten laden** | `pd.read_csv(url)` |
        | **Erkunden** | `.head()`, `.shape`, `.describe()`, `.nunique()` |
        | **Filtern** | `df[df["Spalte"] == "Wert"]` |
        | **Kombinierte Filter** | `df[(Bedingung1) & (Bedingung2)]` |
        | **Sortieren** | `.sort_values("Spalte", ascending=False)` |
        | **Liniendiagramm** | `px.line(df, x=..., y=..., color=...)` |
        | **Balkendiagramm** | `px.bar(df, x=..., y=..., color=...)` |
        | **Beschriftung** | `labels={...}`, `title="..."` |

        ### Nächste Schritte

        Im Projekt wirst du mit einem **anderen Datensatz** der Stadt Zürich arbeiten
        und eigene Visualisierungen erstellen. Mögliche Datensätze:

        - Wetterdaten (Temperatur, Niederschlag)
        - Verkehrszählung (Fahrzeuge pro Stunde)
        - VBZ-Fahrgastzahlen (öffentlicher Verkehr)

        Alle Datensätze findest du unter
        [data.stadt-zuerich.ch](https://data.stadt-zuerich.ch/).
        """
    )
    return


if __name__ == "__main__":
    app.run()
