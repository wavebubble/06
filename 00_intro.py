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
    mo.md("# Willkommen bei marimo! 🌊🍃")
    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 22)
    return (slider,)


@app.cell(hide_code=True)
def _(mo, slider):
    mo.md(f"""
    marimo ist ein **reaktives** Python-Notebook.

    Das bedeutet, dass marimo-Notebooks im Gegensatz zu herkömmlichen Notebooks automatisch ausgeführt werden,
     wenn Sie sie ändern oder
    mit UI-Elementen wie diesem Schieberegler interagieren: {slider}.

    {"##" + "🍃" * slider.value}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Tipp: Automatische Ausführung deaktivieren": mo.md(
                rf"""
            Mit marimo können Sie die automatische Ausführung deaktivieren: Gehen Sie einfach in die
            Notebook-Einstellungen und setzen Sie

            "Runtime > On Cell Change" auf "lazy".

            Wenn die Laufzeit "lazy" ist, markiert marimo nach dem Ausführen einer Zelle deren
            Nachkommen als veraltet, anstatt sie automatisch auszuführen. Mit der
            "lazy"“"-Laufzeit haben Sie die Kontrolle darüber, wann Zellen ausgeführt werden, während
            der Status des Notebooks weiterhin garantiert ist.
            """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Reaktive Ausführung

    Ein marimo-Notebook besteht aus kleinen Blöcken von Python-Code, die als
    Zellen bezeichnet werden.

    marimo liest Ihre Zellen und modelliert die Abhängigkeiten zwischen ihnen: Immer wenn
    eine Zelle, die eine globale Variable definiert, ausgeführt wird, führt marimo
    **automatisch** alle Zellen aus, die auf diese Variable verweisen.

    Durch die Reaktivität bleiben der Programmstatus und die Ausgaben mit Ihrem Code synchronisiert,
    wodurch eine dynamische Programmierumgebung entsteht, die Fehler verhindert, bevor sie
    auftreten.
    """)
    return


@app.cell(hide_code=True)
def _(changed, mo):
    (
        mo.md(
            f"""
            **✨ Nice!** The value of `changed` is now {changed}.

            When you updated the value of the variable `changed`, marimo
            **reacted** by running this cell automatically, because this cell
            references the global variable `changed`.

            Reactivity ensures that your notebook state is always
            consistent, which is crucial for doing good science; it's also what
            enables marimo notebooks to double as tools and  apps.
            """
        )
        if changed
        else mo.md(
            """
            **🌊 See it in action.** In the next cell, change the value of the
            variable  `changed` to `True`, then click the run button.
            """
        )
    )
    return


@app.cell
def _():
    changed = True
    return (changed,)


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Tipp: Ausführungsreihenfolge": (
                """
            Die Reihenfolge der Zellen auf der Seite hat keinen Einfluss auf
            die Reihenfolge, in der die Zellen ausgeführt werden: marimo weiss, dass eine Zelle,
            die eine Variable liest, nach der Zelle ausgeführt werden muss, die  sie definiert. Dadurch
            können Sie Ihren Code so organisieren, wie es für Sie am sinnvollsten ist
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Globale Namen müssen eindeutig sein.** Um Reaktivität zu ermöglichen, legt marimo eine
    Einschränkung hinsichtlich der Darstellung von Namen in Zellen fest: Keine zwei Zellen dürfen dieselbe
    Variable definieren.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Tipp: Ausführungsreihenfolge": (
                """
            Die Reihenfolge der Zellen auf der Seite hat keinen Einfluss auf
            die Reihenfolge, in der die Zellen ausgeführt werden: marimo weiss, dass eine Zelle,
            die eine Variable liest, nach der Zelle ausgeführt werden muss, die  sie definiert. Dadurch
            können Sie Ihren Code so organisieren, wie es für Sie am sinnvollsten ist
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "Tipp: private Variablen": (
                """
                Variablen mit einem Understrich-Präfix sind "privat" und können also in mehreren Zellen vorkommen.
                """
            )
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. UI-Elemente (UI = User Interface)

    Zellen können interaktive UI-Elemente ausgeben. Die Interaktion mit einem UI-Element
    löst **automatisch die Ausführung des Notebooks aus**: Wenn
    Sie mit einem UI-Element interagieren, wird dessen Wert an Python zurückgesendet, und
    jede Zelle, die auf dieses Element verweist, wird erneut ausgeführt.

    marimo bietet eine Bibliothek mit UI-Elementen zur Auswahl in
    `marimo.ui`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **🌊 Einige UI Elemente.** Probiere die Elemente aus.
    """)
    return


@app.cell
def _(mo):
    icon = mo.ui.dropdown(["🍃", "🌊", "✨"], value="🍃")
    return (icon,)


@app.cell
def _(icon, mo):
    repetitions = mo.ui.slider(1, 16, label=f"number of {icon.value}: ")
    return (repetitions,)


@app.cell
def _(icon, repetitions):
    icon, repetitions
    return


@app.cell
def _(icon, mo, repetitions):
    mo.md("# " + icon.value * repetitions.value)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. marimo ist pures Python

    marimo-Zellen analysieren Python (und nur Python), und marimo-Notebooks werden
    als reine Python-Dateien gespeichert – Ausgaben sind _nicht_ enthalten. Es gibt keine
    magische Syntax.

    Die von marimo generierten Python-Dateien sind:

    - leicht mit Git zu versionieren, was zu minimalen Diffs führt
    - sowohl für Menschen als auch für Maschinen lesbar
    - mit einem Tool Ihrer Wahl formatierbar
    - als Python-Skripte verwendbar, wobei UI-Elemente ihre Standardwerte annehmen
    und
    - von anderen Modulen importierbar (mehr dazu in Zukunft).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Notebooks als Apps ausführen

    marimo-Notebooks können auch als Apps verwendet werden. Klicken Sie auf das App-Fenstersymbol unten rechts, um dieses Notebook in der „App-Ansicht” anzuzeigen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. marimo enthält Tutorials:

    - `dataflow`: Weitere Informationen zur automatischen Ausführung von marimo
    - `ui`: Verwendung von UI-Elementen
    - `markdown`: Schreiben von Markdown mit interpolierten Werten und
       LaTeX
    - `plots`: Wie das Plotten in marimo funktioniert
    - `sql`: Verwendung von SQL
    - `layout`: Layout-Elemente in marimo
    - `fileformat`: Wie das Dateiformat von marimo funktioniert
    - `markdown-format`: Verwendung von `.md`-Dateien in marimo
    - `for-jupyter-users`: Wenn Sie von Jupyter kommen

    Zusätzlich zu den Tutorials finden Sie Beispiele in unserem
    [GitHub-Repository](https://www.github.com/marimo-team/marimo/tree/main/examples).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Tipps für den Marimo Editor
    """)
    return


@app.cell
def _(mo, tips):
    mo.accordion(tips)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fun fact
    Der Name "Marimo" bezieht sich auf eine Algenart, die unter
    geeigneten Bedingungen zu kleinen Kugeln zusammenwächst, die als
    "Marimo-Moosbälle" bezeichnet werden. Diese beliebten Gebilde bestehen lediglich aus Algensträngen, sind jedoch mehr als die Summe ihrer Teile.
    """)
    return


@app.cell
def _():
    tips = {
        "Speichern": (
            """
            **Speichern**

            - _Benenne_ deine App über das Feld oben auf dem Bildschirm oder
              mit `Ctrl/Cmd+s`. Du kannst auch über die Kommandozeile eine
              benannte App erstellen, z. B. mit `marimo edit app_name.py`.

            - _Speichere_ durch Klicken auf das Speichern-Symbol unten rechts
              oder durch Eingabe von `Ctrl/Cmd+s`. Standardmäßig ist marimo
              so konfiguriert, dass automatisch gespeichert wird.
            """
        ),
        "Ausführen": (
            """
            1. _Führe eine Zelle aus_, indem du auf den Play-Button ( ▷ )
            oben rechts in der Zelle klickst oder `Ctrl/Cmd+Enter` eingibst.

            2. _Führe eine veraltete Zelle aus_, indem du auf den gelben
            Ausführen-Button rechts neben der Zelle klickst oder
            `Ctrl/Cmd+Enter` eingibst. Eine Zelle ist veraltet, wenn ihr
            Code geändert, aber nicht ausgeführt wurde.

            3. _Führe alle veralteten Zellen aus_, indem du auf den
            Play-Button ( ▷ ) unten rechts auf dem Bildschirm klickst oder
            `Ctrl/Cmd+Shift+r` eingibst.
            """
        ),
        "Konsolenausgabe": (
            """
            Konsolenausgaben (z. B. `print()`-Anweisungen) werden unterhalb
            einer Zelle angezeigt.
            """
        ),
        "Zellen erstellen, verschieben und löschen": (
            """
            1. _Erstelle_ eine neue Zelle über oder unter einer bestehenden,
                indem du auf den Plus-Button links neben der Zelle klickst,
                der beim Darüberfahren mit der Maus erscheint.

            2. _Verschiebe_ eine Zelle nach oben oder unten, indem du sie am
                Griff rechts neben der Zelle ziehst, der beim Darüberfahren
                mit der Maus erscheint.

            3. _Lösche_ eine Zelle durch Klicken auf das Papierkorb-Symbol.
                Hole sie zurück, indem du auf den Rückgängig-Button unten
                rechts auf dem Bildschirm klickst oder `Ctrl/Cmd+Shift+z`
                verwendest.
            """
        ),
        "Automatisches ausführen verhindern": (
            """
            Über die Notebook-Einstellungen (Zahnrad-Symbol) oder das
            Footer-Panel kannst du die automatische Ausführung deaktivieren.
            Das ist hilfreich, wenn du mit rechenintensiven Notebooks oder
            Notebooks arbeitest, die Seiteneffekte wie Datenbank-Transaktionen
            haben.
            """
        ),
        "Zellen deaktivieren": (
            """
            Du kannst eine Zelle über das Kontextmenü der Zelle deaktivieren.
            marimo führt niemals eine deaktivierte Zelle oder Zellen aus,
            die von ihr abhängen. Das kann helfen, versehentliche Ausführung
            teurer Berechnungen beim Bearbeiten eines Notebooks zu verhindern.
            """
        ),
        "Code-Folding": (
            """
            Du kannst den Code in einer Zelle einklappen, indem du auf die
            Pfeil-Symbole in der Zeilennummernspalte links klickst oder
            Tastenkürzel verwendest.

            Verwende die Befehlspalette (`Ctrl/Cmd+k`) oder ein Tastenkürzel,
            um schnell alle Zellen ein- oder auszuklappen.
            """
        ),
        "Code-Formatierung": (
            """
            Wenn du [ruff](https://github.com/astral-sh/ruff) installiert
            hast, kannst du eine Zelle mit dem Tastenkürzel `Ctrl/Cmd+b`
            formatieren.
            """
        ),
        "Befehlspalette": (
            """
            Verwende `Ctrl/Cmd+k`, um die Befehlspalette zu öffnen.
            """
        ),
        "Keyboard Shortcuts": (
            """
            Öffne das Notebook-Menü (oben rechts) oder gib `Ctrl/Cmd+Shift+h`
            ein, um eine Liste aller Tastenkürzel anzuzeigen.
            """
        ),
        "Konfiguration": (
            """
           Konfiguriere den Editor, indem du auf das Zahnrad-Symbol nahe der
           oberen rechten Ecke des Bildschirms klickst.
           """
        ),
        "Abmelden": (
            """
           Du kannst Marimo verlassen und den Server herunterfahren, indem du
           auf den Logout-Button oben rechts auf dem Bildschirm klickst.

           :floppy_disk: _Speichere unbedingt zuerst deine Arbeit!_ 
           """
        ),
    }
    return (tips,)


if __name__ == "__main__":
    app.run()
