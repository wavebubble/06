# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo>=0.20.1",
# ]
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
    #Python in Beispielen: Eine Einführung für Programmierer:innen

    T. Kohn
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1 Listen und Summen

    Die Primzahlen eignen sich hervorragend als Beispiel-Liste, weil die Zahlen nicht regelmässig verteilt sind. In diesem Abschnitt stellen wir verschiedene Techniken vor, um die Summe einer Liste von Primzahlen (oder anderem) zu berechnen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### For-Schleife
    """)
    return


@app.cell
def _():
    # For-Schleifen in Python arbeiten immer mit Listen
    primes_1 = [2, 3, 5, 7, 11, 13, 17, 19]
    summe_1 = 0
    for p in primes_1:
        summe_1 += p
    print(summe_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Funktionen
    """)
    return


@app.cell
def _():
    # In Python wird eine Funktion mit def definiert
    def summe_funktion(liste):
        result = 0
        for zahl in liste:
            result += zahl
        return result

    primes_2 = [2, 3, 5, 7, 11, 13, 17, 19]
    print(summe_funktion(primes_2))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Eine Funktion für alles
    """)
    return


@app.cell
def _():
    def head(liste):
        return liste[0] if liste else None

    def tail(liste):
        return liste[1:] if liste else []

    return head, tail


@app.cell
def _(head, tail):
    # Weil Variablen in Python keinen festen Typ haben, können wir die 
    # Summenfunktion auch so umschreiben, dass sie Strings zusammenhängt
    def summe_generic(liste):
        if liste != []:
            result = head(liste)
            for item in tail(liste):
                result += item
            return result
        else:
            return None

    primes_3 = [2, 3, 5, 7, 11, 13, 17, 19]
    print(summe_generic(primes_3))
    print(summe_generic(["Tic", "Tac", "Toe"]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Rekursion
    """)
    return


@app.cell
def _(head, tail):
    # head(liste) gibt das erste Element zurück, 
    # tail(liste) den Rest – wiederum als Liste
    def summe_rekursiv(liste):
        if liste == []:
            return 0
        else:
            return head(liste) + summe_rekursiv(tail(liste))

    primes_4 = [2, 3, 5, 7, 11, 13, 17, 19]
    print(summe_rekursiv(primes_4))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Für Profis: Falten*
    """)
    return


@app.cell
def _(head, tail):
    # Wir machen sogar die «Addition» austauschbar
    def fold(liste, op):
        result = head(liste)
        for item in tail(liste):
            result = op(result, item)
        return result

    def add(x, y):
        return x + y

    def mul(x, y):
        return x * y

    primes_5 = [2, 3, 5, 7, 11, 13, 17, 19]
    print(fold(primes_5, add))
    print(fold(primes_5, mul))
    return (fold,)


@app.cell
def _(fold):
    # Lambda-Ausdrücke verwenden
    primes_6 = [2, 3, 5, 7, 11, 13, 17, 19]
    print(fold(primes_6, lambda x, y: x + y))
    print(fold(primes_6, lambda x, y: x * y))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 2 Fibonacci-Zahlen berechnen

    Die Fibonacci-Zahlen sind das klassische Beispiel für eine rekursiv definierte Zahlenfolge:

    $a_n = a_{n-2} + a_{n-1}$, $a_0 = a_1 = 1$

    1, 1, 2, 3, 5, 8, 13, 21, ...
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Der naive Ansatz
    """)
    return


@app.cell
def _():
    # Dieser Ansatz hat eine exponentielle Laufzeit!
    def fib_naive(n):
        if n < 2:
            return 1
        else:
            return fib_naive(n-2) + fib_naive(n-1)

    print(fib_naive(10))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Iterativer Ansatz mit Liste
    """)
    return


@app.cell
def _():
    def fib_liste(n):
        F = [1, 1]
        for _ in range(n-1):
            x = F[-2] + F[-1]
            F.append(x)
        return F[-1]

    print(fib_liste(30))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Iterativer Ansatz ohne Liste
    """)
    return


@app.cell
def _():
    # Mit Tupeln arbeiten
    def fib_tupel(n):
        (a, b) = (1, 1)
        for _ in range(n-1):
            (a, b) = (b, a+b)
        return b

    print(fib_tupel(30))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Memoization: Rekursion mit Liste
    """)
    return


@app.cell
def _():
    memo_table_1 = {}
    def fib_memo_1(n):
        if n < 2:
            return 1
        elif n in memo_table_1:
            return memo_table_1[n]
        else:
            result = fib_memo_1(n-2) + fib_memo_1(n-1)
            memo_table_1[n] = result
            return result

    print(fib_memo_1(30))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Kürzere Variante mit Memoization
    """)
    return


@app.cell
def _():
    memo_table_2 = {0: 1, 1: 1}
    def fib_memo_2(n):
        if n not in memo_table_2:
            memo_table_2[n] = fib_memo_2(n-2) + fib_memo_2(n-1)
        return memo_table_2[n]

    print(fib_memo_2(30))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Dictionaries
    """)
    return


@app.cell
def _():
    # Neben Listen sind auch Dictionaries in Python fest eingebaute Datenstrukturen
    BDFL = {"Name": "van Rossum", "Vorname": "Guido",
            "Geb-Jahr": 1956, "BDFL": True}
    PT = {(3, 4): 5, (5, 12): 13, (20, 21): 29}

    print("Name", BDFL["Name"])
    print(PT[(5, 12)])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3 Listen: Chaos und Ordnung
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Zufallszahlen
    """)
    return


@app.cell
def _():
    from random import randint
    liste_1 = []
    for _ in range(30):
        liste_1.append(randint(0, 20))
    print(liste_1)
    return (randint,)


@app.cell
def _(randint):
    # Mit List-Comprehensions kürzer
    liste_2 = [randint(0, 20) for x in range(30)]
    print(liste_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Zahlen binär zerlegen
    """)
    return


@app.cell
def _():
    # Jede ganze Zahl lässt sich auch binär schreiben
    binary_list = []
    zahl_bin = 69
    for _ in range(8):
        binary_list.insert(0, zahl_bin % 2)
        zahl_bin = zahl_bin // 2
    print(binary_list)
    return (binary_list,)


@app.cell
def _(binary_list):
    # Mit join werden die einzelnen Ziffern zu einem String verbunden
    print(''.join(map(str, binary_list)))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Sortieren (I)
    """)
    return


@app.cell
def _():
    def my_sort_1(liste):
        result = []
        while liste != []:
            x = min(liste)
            liste.remove(x)  # x aus alter Liste entfernen
            result.append(x)  # x an neue Liste anhängen
        return result

    print(my_sort_1([14, 3, 4, 5, 17, 7, 18, 11, 19]))
    print(my_sort_1(["Kuh", "Biene", "Zebra", "Emu", "Affe"]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Sortieren (II)
    """)
    return


@app.cell
def _():
    def my_sort_2(liste):
        result = []
        for item in liste:
            inserted = False
            for i in range(len(result)):
                if result[i] > item:
                    result.insert(i, item)
                    inserted = True
                    break
            if not inserted:
                result.append(item)
        return result

    print(my_sort_2([14, 3, 4, 5, 17, 7, 18, 11, 19]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Sortieren (III): Merge-Sort
    """)
    return


@app.cell
def _(head, tail):
    def merge_sort(liste):
        if len(liste) <= 1:
            return liste
        # Liste aufteilen und Teile sortieren:
        idx = len(liste) // 2
        partA = merge_sort(liste[:idx])
        partB = merge_sort(liste[idx:])
        # Teillisten miteinander verschmelzen:
        result = []
        while partA != [] and partB != []:
            if head(partA) < head(partB):
                result.append(head(partA))
                partA = tail(partA)
            else:
                result.append(head(partB))
                partB = tail(partB)
        # Entweder partA oder partB ist hier leer:
        return result + partA + partB

    print(merge_sort([4, 9, 1, 7, 5, 3]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Filtern
    """)
    return


@app.cell
def _():
    def filter_funktion(liste, allowed):
        result = []
        for item in liste:
            if item in allowed:
                result.append(item)
        return result

    print(filter_funktion([4, -3, 0, 2, -5], [0, 2, 4, 6, 8]))
    return


@app.cell
def _():
    # Kurzversion mit List Comprehensions
    def filter_short(liste, allowed):
        return [x for x in liste if x in allowed]

    print(filter_short([4, -3, 0, 2, -5], [0, 2, 4, 6, 8]))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4 Listen: Punkte und Polygone

    Punkte lassen sich in Python direkt mit Tupeln abbilden. Ein Tupel ist eine «unveränderbare» Liste. Für ein Polygon verwenden wir dann eine Liste von Tupeln.
    """)
    return


@app.cell
def _():
    # Gleichseitiges Dreieck
    coords_dreieck = [(-34.6, -20), (0, 40), (34.6, -20)]
    print(coords_dreieck)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Distanzen
    """)
    return


@app.cell
def _():
    from math import sqrt

    def dist(p0, p1):
        (x0, y0) = p0
        (x1, y1) = p1
        d = (x1 - x0)**2 + (y1 - y0)**2
        return sqrt(d)

    coords_dist = [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4)]
    min_point = coords_dist[0]
    min_dist = dist(min_point, (0, 0))
    for point in coords_dist:
        d = dist(point, (0, 0))
        if d < min_dist:
            min_dist = d
            min_point = point
    print(min_point)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Graphen
    """)
    return


@app.cell
def _():
    coords_graph_1 = []
    for x in range(-10, 11):
        coords_graph_1.append((5*x, x**2))
    print(coords_graph_1)
    return


@app.cell
def _():
    # Kürzer mit List Comprehension
    coords_graph_2 = [(5*x, x**2) for x in range(-10, 11)]
    print(coords_graph_2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5 Strings: Text analysieren

    Python kann relativ gut mit Strings (Zeichenketten) umgehen und bietet eine Vielzahl von Funktionen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Buchstaben zählen
    """)
    return


@app.cell
def _():
    def count_e(text):
        count = 0
        for letter in text:
            if letter in ["e", "E"]:
                count += 1
        return count

    print(count_e("Python lernen macht Spass!"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Frequenzanalyse
    """)
    return


@app.cell
def _():
    def freq_analysis(text):
        # Tabelle enthält zur Zeit nur Eintrag für 'a' und 'e'.
        letters = {"a": 0, "e": 0}
        for ch in text:
            ch = ch.lower()  # Alles in Kleinbuchstaben
            if ch in letters:
                # Vorhandenen Wert erhöhen:
                letters[ch] += 1
            else:
                # Neuer Eintrag wird automatisch erstellt:
                letters[ch] = 1
        return letters

    print(freq_analysis("Python lernen ist cool!"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Wörter zählen
    """)
    return


@app.cell
def _():
    def count_words(text):
        words = text.split(" ")
        return len(words)

    print(count_words("Python ist auch eine Schlange."))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Parsen einer Zahl
    """)
    return


@app.cell
def _():
    # Liest aus einem String eine hexadezimale Zahl heraus
    eingabe_hex = "3F"
    zahl_hex = 0
    for ch_hex in eingabe_hex.upper():
        zahl_hex *= 0x10
        if '0' <= ch_hex <= '9':
            zahl_hex += (ord(ch_hex) - ord('0'))
        elif 'A' <= ch_hex <= 'F':
            zahl_hex += (ord(ch_hex) - ord('A') + 10)
        else:
            print("Fehler: Ungültiges Zeichen", ch_hex)
            break
    print(zahl_hex)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## AUFGABEN
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **1.** Schreibe eine Funktion fakult(n), die die Fakultät n! = 1·2·3···n einer Zahl n berechnet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **2.** Ein altes Rätsel von Sam Loyd: Finde aus den Zahlen 25, 27, 3, 12, 6, 15, 9, 30, 21, 19 jene heraus, die zusammen die Summe 50 ergeben.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **3.** Schreibe eine Funktion, die aus einer gegebenen Liste alle doppelt vorkommenden Elemente entfernt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **4.** Schreibe eine Funktion, die zwei Listen vergleicht und die Anzahl der Elemente zurückgibt, die in beiden Listen vorkommen.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **5.** Schreibe eine Funktion, die zu einer gegebenen Liste eine zufällige Permutation erzeugt und zurückgibt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **9.** Schreibe eine Funktion center, die den Schwerpunkt eines Polygons berechnet.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **10.** Schreibe eine Funktion circumference, die den Umfang des Polygons ermittelt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **14.** Schreibe die Funktion count_words so um, dass sie Wörter wie «Python-Kurs» als zwei eigene Wörter zählt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **15.** Schreibe ein Programm, das einen Text mit der Caesar-Chiffre verschlüsselt.
    """)
    return


if __name__ == "__main__":
    app.run()
