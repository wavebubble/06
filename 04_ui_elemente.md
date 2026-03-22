# Marimo UI-Elemente — Übersicht

Marimo bietet interaktive UI-Elemente, die automatisch mit Python synchronisiert werden.
Wenn du z.B. einen Slider verschiebst, werden alle Zellen, die den Slider verwenden, automatisch neu ausgeführt.

**Dokumentation:** [docs.marimo.io/api/inputs](https://docs.marimo.io/api/inputs/)

---

## Wichtige Regeln

### 1. UI-Element und `.value` müssen in getrennten Zellen sein

```python
# ZELLE 1: Element erstellen und anzeigen
slider = mo.ui.slider(start=2000, stop=2024, value=2020, label="Jahr:")
slider                  # ← Anzeigen als letzter Ausdruck
return slider,          # ← Weitergeben an andere Zellen

# ZELLE 2: Wert verwenden (slider als Parameter)
jahr = slider.value     # ← Hier erst auf .value zugreifen
df_filtered = df[df["Jahr"] == jahr]
```

> **Fehler wenn beides in einer Zelle steht:**
> `RuntimeError: Accessing the value of a UIElement in the cell that created it is not allowed.`

### 2. Plots in `if/else` werden nicht angezeigt

Verwende `mo.stop()` statt `if/else`:

```python
# FALSCH — Plot wird nicht angezeigt:
if len(daten) == 0:
    mo.md("Keine Daten")
else:
    fig = px.line(daten, ...)
    fig

# RICHTIG — mo.stop() bricht ab und zeigt Fehlermeldung:
mo.stop(len(daten) == 0, mo.md("Keine Daten gefunden."))
fig = px.line(daten, ...)
fig
```

### 3. Jede Variable nur einmal definieren

Eine Variable darf nur in **einer** Zelle definiert werden. Nicht `mo` oder `px` in mehreren Zellen importieren!

---

## Slider

Zahlenwert über einen Schieberegler wählen.

**Zelle 1 — Element erstellen:**
```python
slider = mo.ui.slider(
    start=1950,
    stop=2024,
    value=2000,
    step=1,
    label="Jahrgang wählen:",
    show_value=True,
)
slider
return slider,
```

**Zelle 2 — Wert verwenden:**
```python
jahr = slider.value
gefiltert = df[df["Jahrgang"] == jahr]
```

**Doku:** [docs.marimo.io/api/inputs/slider](https://docs.marimo.io/api/inputs/slider/)

---

## Dropdown

Einen Wert aus einer Liste auswählen.

**Zelle 1:**
```python
dropdown = mo.ui.dropdown(
    options=["weiblich", "männlich"],
    value="weiblich",
    label="Geschlecht:",
)
dropdown
return dropdown,
```

**Zelle 2:**
```python
geschl = dropdown.value
gefiltert = df[df["SexLang"] == geschl]
```

**Mit Werten aus dem Datensatz:**
```python
# Optionen direkt aus einer Spalte generieren
staedte = sorted(df["Stadt"].unique().tolist())
dropdown = mo.ui.dropdown(options=staedte, value=staedte[0], label="Stadt:")
dropdown
return dropdown,
```

**Doku:** [docs.marimo.io/api/inputs/dropdown](https://docs.marimo.io/api/inputs/dropdown/)

---

## Textfeld

Freie Texteingabe, z.B. für einen Namen.

**Zelle 1:**
```python
textfeld = mo.ui.text(
    value="Anna",
    label="Name eingeben:",
    full_width=False,
)
textfeld
return textfeld,
```

**Zelle 2:**
```python
name = textfeld.value.strip()
gefiltert = df[df["Vorname"] == name]
mo.stop(len(gefiltert) == 0, mo.md(f"**{name}** nicht gefunden."))
fig = px.line(gefiltert, x="Jahrgang", y="Anzahl", title=f"Vorname: {name}")
fig
```

**Doku:** [docs.marimo.io/api/inputs/text](https://docs.marimo.io/api/inputs/text/)

---

## Checkbox

Ja/Nein-Auswahl (gibt `True` oder `False` zurück).

**Zelle 1:**
```python
checkbox = mo.ui.checkbox(label="Logarithmische Skala verwenden")
checkbox
return checkbox,
```

**Zelle 2:**
```python
fig = px.line(df, x="Jahr", y="Wert", log_y=checkbox.value)
fig
```

**Doku:** [docs.marimo.io/api/inputs/checkbox](https://docs.marimo.io/api/inputs/checkbox/)

---

## Number

Zahl eingeben (mit optionalem Bereich).

**Zelle 1:**
```python
anzahl = mo.ui.number(
    start=1,
    stop=50,
    value=10,
    label="Anzahl Top-Einträge:",
)
anzahl
return anzahl,
```

**Zelle 2:**
```python
top = df.sort_values("Wert", ascending=False).head(anzahl.value)
```

**Doku:** [docs.marimo.io/api/inputs/number](https://docs.marimo.io/api/inputs/number/)

---

## Radio Buttons

Eine Option aus einer Gruppe wählen.

**Zelle 1:**
```python
diagrammtyp = mo.ui.radio(
    options=["Liniendiagramm", "Balkendiagramm", "Streudiagramm"],
    value="Liniendiagramm",
    label="Diagrammtyp:",
)
diagrammtyp
return diagrammtyp,
```

**Zelle 2:**
```python
if diagrammtyp.value == "Liniendiagramm":
    fig = px.line(df, x="Jahr", y="Wert")
elif diagrammtyp.value == "Balkendiagramm":
    fig = px.bar(df, x="Jahr", y="Wert")
else:
    fig = px.scatter(df, x="Jahr", y="Wert")
fig
```

**Doku:** [docs.marimo.io/api/inputs/radio](https://docs.marimo.io/api/inputs/radio/)

---

## Date Picker

Ein Datum auswählen.

**Zelle 1:**
```python
datum = mo.ui.date(value="2024-01-01", label="Datum wählen:")
datum
return datum,
```

**Zelle 2:**
```python
gewaehltes_datum = datum.value  # → datetime.date Objekt
```

**Doku:** [docs.marimo.io/api/inputs/date](https://docs.marimo.io/api/inputs/date/)

---

## Mehrere Elemente anordnen

Mit `mo.hstack()` (nebeneinander) und `mo.vstack()` (untereinander) kannst du Elemente gruppieren:

```python
# Nebeneinander
mo.hstack([slider, dropdown], gap=2)

# Untereinander
mo.vstack([slider, dropdown])
```

**Doku:** [docs.marimo.io/api/layouts](https://docs.marimo.io/api/layouts/)

---

## Zusammenfassung

| Element | Code | `.value` liefert |
|---------|------|------------------|
| Slider | `mo.ui.slider(start, stop, value, label)` | `int` oder `float` |
| Dropdown | `mo.ui.dropdown(options, value, label)` | Gewählte Option (`str`) |
| Textfeld | `mo.ui.text(value, label)` | Eingegebener Text (`str`) |
| Checkbox | `mo.ui.checkbox(label)` | `True` / `False` |
| Number | `mo.ui.number(start, stop, value, label)` | `int` oder `float` |
| Radio | `mo.ui.radio(options, value, label)` | Gewählte Option (`str`) |
| Datum | `mo.ui.date(value, label)` | `datetime.date` |

**Alle UI-Elemente:** [docs.marimo.io/api/inputs](https://docs.marimo.io/api/inputs/)

**Interaktivitäts-Guide:** [docs.marimo.io/guides/interactivity](https://docs.marimo.io/guides/interactivity/)
