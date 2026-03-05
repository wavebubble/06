# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.20.4",
# ]
# ///

import marimo

__generated_with = "0.20.1"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Rekursion & Memoization

    Du kennst `fib()` und `summe()` aus dem Skript.
    In diesem Notebook vertiefst du diese Ideen.

    **Lernziele:**
    - Rekursive Funktionen lesen, verstehen und schreiben
    - Das Problem der exponentiellen Laufzeit erkennen
    - Memoization mit einem Dictionary anwenden
    - Eine eigene Wegsuche für eine Snake-Challenge bauen
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Teil 1 – Rekursion
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1a – Fibonacci nochmals anschauen

    Aus dem Skript kennst du bereits den naiven rekursiven Ansatz:

    ```python
    def fib(n):
        if n < 2:
            return 1
        else:
            return fib(n-2) + fib(n-1)
    ```

    Führe die Zelle unten aus und beobachte, wie lange `fib(35)` dauert.
    """)
    return


@app.cell
def _():
    import time

    def fib(n):
        if n < 2:
            return 1
        else:
            return fib(n-2) + fib(n-1)

    start = time.time()
    resultat = fib(35)
    dauer = time.time() - start
    print("Resultat:",resultat,"Dauer:",dauer)
    return (time,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1b – Warum ist das so langsam?

    Zeichne den Rekursionsbaum für `fib(5)` von Hand auf ein Blatt Papier.
    Wie oft wird `fib(2)` aufgerufen?

    **Beobachtung:** Viele Teilprobleme werden mehrfach berechnet.
    Bei `fib(35)` passiert das millionenfach.

    > 💡 Die Anzahl Aufrufe wächst ungefähr (eine Baumseite ist kürzer) wie **2ⁿ** –
    > das nennt man **exponentielle Laufzeit**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1c – Aufgabe: Potenz rekursiv

    Schreibe eine rekursive Funktion `potenz(basis, exp)`,
    die `basis`^`exp` berechnet – **ohne** den `**`-Operator.

    Tipp: Was ist der Basisfall? Was ist der rekursive Schritt?

    ```
    potenz(2, 0) = 1
    potenz(2, 1) = 2
    potenz(2, 4) = 2 * potenz(2, 3)
    ```
    """)
    return


@app.cell
def _():
    def potenz(basis, exp):
        # TODO: Basisfall

        # TODO: rekursiver Schritt

        pass

    # Teste deine Funktion:
    print(potenz(2, 0))   # erwartet: 1
    print(potenz(2, 8))   # erwartet: 256
    print(potenz(3, 4))   # erwartet: 81
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 1d – Aufgabe: Palindrom prüfen

    Ein Palindrom ist ein Wort, das vorwärts und rückwärts gleich lautet
    (z.B. «racecar», «level», «anna»).

    Schreibe eine **rekursive** Funktion `ist_palindrom(s)`.

    Tipp: Ein String ist ein Palindrom, wenn...
    - er leer ist oder nur einen Buchstaben hat (Basisfall), **oder**
    - der erste und letzte Buchstabe gleich sind **und**
      der mittlere Teil ebenfalls ein Palindrom ist.

    In Python: `s[0]` = erster, `s[-1]` = letzter, `s[1:-1]` = Mitte.
    """)
    return


@app.cell
def _():
    def ist_palindrom(s):
        # TODO

        # Prüfe, ob die äusseren Buchstaben gleich sind

        # Rekursiver Schritt: Schneide vorne und hinten ab und prüfe den Rest

        return False

    print(ist_palindrom("Anna"))      # True
    print(ist_palindrom("Uhu"))       # True
    print(ist_palindrom("Level"))     # True
    print(ist_palindrom("Python"))    # False
    print(ist_palindrom(""))          # True
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Teil 2 – Memoisierung
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2a – Die Idee

    Das Problem bei `fib`: dieselben Teilprobleme werden
    immer wieder neu berechnet.

    Die Lösung: **Memoisierung** – wir merken uns bereits berechnete
    Resultate in einem Dictionary.

    ```
    memo = {}          # leere Tabelle

    erstes Mal:   fib(10) wird berechnet → in memo gespeichert
    zweites Mal:  fib(10) wird aus memo gelesen → sofort fertig
    ```

    Schaue dir diesen Code an – er stammt direkt aus dem Skript:
    """)
    return


@app.cell
def _(time):
    memo_fib = {0: 1, 1: 1}

    def fib_memo(n):
        if n not in memo_fib:
            memo_fib[n] = fib_memo(n-2) + fib_memo(n-1)
        return memo_fib[n]

    start2 = time.time()
    resultat2 = fib_memo(35)
    dauer2 = time.time() - start2

    print(f"fib(35) = {resultat2}")
    print(f"Laufzeit: {dauer2:.6f} Sekunden")
    print(f"Inhalt von memo_fib (erste 5 Einträge): { {k: memo_fib[k] for k in list(memo_fib)[:5]} }")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2b – Aufgabe: Potenz mit Memoisierung

    Erweitere deine `potenz()`-Funktion aus 1c mit Memoisierung.

    Das Muster ist immer gleich:

    ```python
    memo = {}

    def funktion(n):
        if n in memo:
            return memo[n]
        # ... berechnen ...
        memo[n] = resultat
        return resultat
    ```
    """)
    return


@app.cell
def _():
    memo_potenz = {}

    def potenz_memo(basis, exp):
        key = (basis, exp)
        if key in memo_potenz:
            return memo_potenz[key]
        # TODO: Basisfall und rekursiver Schritt
        # memo_potenz[key] = ...
        pass

    print(potenz_memo(2, 8))    # 256
    print(potenz_memo(3, 4))    # 81
    print(f"Tabelle: {memo_potenz}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2c – Aufgabe: Münzwechsel

    Du hast Münzen der Werte `[1, 5, 10, 20]` Rappen.
    Schreibe eine Funktion `wechsel(betrag, muenzen)`,
    die die **minimale Anzahl Münzen** zurückgibt,
    um genau `betrag` Rappen zu erreichen.

    Beispiel:
    ```
    wechsel(36, [1, 5, 10, 20]) = 3   # 20 + 10 + 5 + 1 → nein, 20+10+5+1=36, 4 Münzen
                                       # 20 + 10 + 5 + 1 = 36 → 4 Münzen
    wechsel(30, [1, 5, 10, 20]) = 2   # 20 + 10
    wechsel(11, [1, 5, 10, 20]) = 2   # 10 + 1
    ```

    **Rekursive Idee:**
    Für jede Münze `m` die kleiner als `betrag` ist:
    → berechne `1 + wechsel(betrag - m, muenzen)`
    → nimm das Minimum davon

    Basisfall: `betrag == 0` → 0 Münzen nötig

    **Erweitere die Funktion danach mit Memoization.**
    """)
    return


@app.cell
def _():
    def wechsel(betrag, muenzen, memo=None):
        if memo is None:
            memo = {}
        # TODO: Basisfall
        # TODO: Key für memo
        # TODO: rekursiver Schritt mit min()
        pass

    print(wechsel(11,  [1, 5, 10, 20]))   # 2
    print(wechsel(30,  [1, 5, 10, 20]))   # 2
    print(wechsel(36,  [1, 5, 10, 20]))   # 4
    print(wechsel(100, [1, 5, 10, 20]))   # 5
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---
    ## Teil 3 – Wegsuche
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3a – Das Snake-Problem

    **Gibt es überhaupt einen Weg zum Futter – ohne in eine Wand oder den Körper zu laufen?**

    Wir modellieren das Spielfeld als einfaches 2D-Gitter.
    Hindernisse sind in einem `set` gespeichert (schnelles Nachschlagen!). Der Unterschied von einem `set` zu einer Liste ist, dass bei einem `set` Elemente nicht doppelt vorkommen und sehr rasch geprüft werden kann, ob ein Element in einem `set` vorhanden ist. Listen haben einen Index, der durchlaufen wird bei einer Element-Suche, was die Suche verlangsamt.

    ```
    . . . . F
    . X X . .
    . . X . .
    S . . . .
    ```
    S = Start, F = Futter, X = Hindernis

    Schreibe eine rekursive Funktion `erreichbar(pos, ziel, hindernisse, besucht)`,
    die `True` zurückgibt wenn `ziel` von `pos` aus erreichbar ist.

    **Basisfall:** `pos == ziel`

    **Rekursiver Schritt:** Für jeden Nachbarn von `pos`:
    - nicht in `hindernisse`
    - noch nicht `besucht`
    - → rekursiv prüfen

    `besucht` ist ein `set` – füge `pos` am Anfang hinzu,
    damit du keine Kreise läufst.
    """)
    return


@app.cell
def _():
    def nachbarn(pos, breite=10, hoehe=10):
        """Gibt alle gültigen Nachbarfelder von pos zurück."""
        x, y = pos
        alle = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        return [(nx, ny) for (nx, ny) in alle
                if 0 <= nx < breite and 0 <= ny < hoehe]

    def erreichbar(pos, ziel, hindernisse, besucht):
        # TODO
        pass

    # Test:
    hindernisse = {(1,1), (2,1), (2,2)}
    print(erreichbar((0,0), (4,4), hindernisse, set()))   # True
    print(erreichbar((0,0), (4,4), {(0,1),(1,0)}, set())) # False (eingesperrt)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3b – Aufgabe: Kürzester Weg mit Memoisierung

    Erweitere `erreichbar()` zu einer Funktion
    `kuerzester_weg(pos, ziel, hindernisse, schritte, memo)`,
    die die **minimale Anzahl Schritte** zurückgibt,
    um von `pos` nach `ziel` zu kommen.

    Falls kein Weg existiert: gib `float("inf")` zurück.

    **Key für memo:** `(pos, schritte)` – wie im `fib`-Beispiel.

    > 💡 Warum `schritte` im Key? Weil dieselbe Position mit
    > unterschiedlich vielen verbleibenden Schritten zu
    > unterschiedlichen Resultaten führen kann!
    """)
    return


@app.cell
def _():
    def kuerzester_weg(pos, ziel, hindernisse, schritte, memo=None):
        if memo is None:
            memo = {}
        key = (pos, schritte)
        if key in memo:
            return memo[key]
        # TODO: Basisfall pos == ziel
        # TODO: Basisfall schritte == 0 (kein Weg gefunden)
        # TODO: rekursiv alle Nachbarn probieren, Minimum nehmen
        # memo[key] = ...
        pass

    # Test:
    hindernisse = {(1,1), (2,1), (2,2)}
    print(kuerzester_weg((0,0), (4,4), hindernisse, schritte=20, memo={}))  # 8
    print(kuerzester_weg((0,0), (4,0), set(),       schritte=10, memo={}))  # 4
    return (kuerzester_weg,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3c – Vom Weg zur Bot-Entscheidung

    Du hast jetzt alle Zutaten für einen echten Snake-Bot.

    Der letzte Schritt: Nutze `kuerzester_weg()`,
    um die **beste Richtung** zu wählen.

    ```python
    richtungen = [(1,0), (-1,0), (0,1), (0,-1)]

    def bester_zug(kopf, futter, hindernisse):
        beste_richtung = None
        beste_distanz  = float("inf")

        for (dx, dy) in richtungen:
            naechste_pos = (kopf[0]+dx, kopf[1]+dy)
            if naechste_pos not in hindernisse:
                d = kuerzester_weg(naechste_pos, futter,
                                   hindernisse, schritte=30, memo={})
                if d < beste_distanz:
                    beste_distanz  = d
                    beste_richtung = (dx, dy)

        return beste_richtung
    ```

    **Aufgabe:** Teste `bester_zug()` mit verschiedenen Szenarien.
    Was passiert wenn das Futter eingesperrt ist?
    Wie verhält sich der Bot wenn `schritte` sehr klein ist?
    """)
    return


@app.cell
def _(kuerzester_weg):
    richtungen = [(1,0), (-1,0), (0,1), (0,-1)]

    def bester_zug(kopf, futter, hindernisse):
        beste_richtung = None
        beste_distanz  = float("inf")
        for (dx, dy) in richtungen:
            naechste_pos = (kopf[0]+dx, kopf[1]+dy)
            if naechste_pos not in hindernisse:
                d = kuerzester_weg(naechste_pos, futter,
                                   hindernisse, schritte=30, memo={})
                if d < beste_distanz:
                    beste_distanz  = d
                    beste_richtung = (dx, dy)
        return beste_richtung

    # Szenario 1: freies Feld
    print("Szenario 1:", bester_zug((0,0), (4,4), set()))

    # Szenario 2: Hindernis auf direktem Weg
    print("Szenario 2:", bester_zug((0,0), (4,0), {(1,0),(2,0),(3,0)}))

    # Szenario 3: Futter eingesperrt – was gibt der Bot zurück?
    print("Szenario 3:", bester_zug((0,0), (5,5), {(4,5),(5,4),(6,5),(5,6)}))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Zusammenfassung

    | Technik | Laufzeit | Wann? |
    |---|---|---|
    | Naive Rekursion | O(2ⁿ) | Kleine Probleme |
    | Memoization | O(n) bis O(n²) | Wenn Teilprobleme sich wiederholen |

    **Das Muster ist immer dasselbe:**

    ```python
    memo = {}

    def f(n):
        if n in memo:
            return memo[n]
        # ... berechnen ...
        memo[n] = resultat
        return resultat
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Bonusaufgabe: Laufzeit sichtbar machen

    Zähle wie viele Funktionsaufrufe `fib_naiv` und `fib_memo`
    jeweils brauchen – und zeichne den Unterschied als Tabelle.

    Tipp: Verwende eine globale Variable als Zähler.

    ```python
    aufrufe = 0

    def fib_mit_zaehler(n):
        global aufrufe
        aufrufe += 1
        ...
    ```
    """)
    return


@app.cell
def _():
    # Bonusaufgabe hier:
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
