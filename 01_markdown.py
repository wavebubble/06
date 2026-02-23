# /// script
# dependencies = [
#     "marimo",
# ]
# requires-python = ">=3.12"
# ///

import marimo

__generated_with = "0.20.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Markdown mit Python
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Verwende `mo.md` mit einem `f-string` (Format-String) um Markdown mit Python-Objekten zu verwenden.
    """)
    return


@app.cell
def _():
    name = "Alice"
    return (name,)


@app.cell(hide_code=True)
def _(mo, name):
    mo.md(rf"""
    Hallo, {name}!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Verwende Marimo-UI-Elemente direkt in Markdown:
    """)
    return


@app.cell
def _(mo):
    text_input = mo.ui.text(placeholder="My name is ...", debounce=False)
    return (text_input,)


@app.cell(hide_code=True)
def _(mo, text_input):
    mo.md(rf"""
    Wie heisst du? {text_input}

    Hallo, {text_input.value}!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Graphen und Datenstrukturen kannst du in `mo.as_html()` einbinden:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(f"""
    Eine Liste mit Zahlen:

    {mo.as_html([1, 2, 3])}
    """)
    return


if __name__ == "__main__":
    app.run()
