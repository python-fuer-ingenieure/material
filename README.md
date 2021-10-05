# Python für Ingenieure für Dummies

Dieses Repo enthält das Begleitmaterial für das Buch **[Python für Ingenieure für Dummies](https://www.wiley-vch.de/de?option=com_eshop&view=product&isbn=9783527717675)**, erschienen im Wiley-VCH Verlag, 2021. Inhaltsverzeichnis, Probekapitel und Index sind auf der [Verlags-Website](https://www.wiley-vch.de/de?option=com_eshop&view=product&isbn=9783527717675) abrufbar.


[<img src="img/cover_book.png" title="Python für Ingenieure für Dummies" alt="Cover: Python für Ingenieure für Dummies" width="300">](https://www.wiley-vch.de/de?option=com_eshop&view=product&isbn=9783527717675)


## Zusammenhang zwischen Begleitmaterial und Buch

Alle Code-Beispiele ("Schnipsel") im Buch sind kapitelweise in Jupyter-Notebooks hinterlegt und können auf diese Weise direkt (ohne abtippen) ausgeführt werden. Viele der Beispiele erzeugen eine grafische Ausgabe die direkt der jeweiligen Abbildung im Buch entspricht. Damit ist die **Reproduzierbarkeit** der Ergebnisse gewährleistet.

Die Schnipsel im Buch wurden aus den Notebooks mit einem Skript erzeugt. Alle Code-Zeilen zwischen speziellen Markdown-Zellen (`begin XYZ` und `end`) werden zu einem Schnipsel für das Buch zusammengefasst – bis auf die Zeilen, die mit  dem speziellen Kommentar `#!` enden. Diese werden aus didaktischen Gründen ausgespart. Aus ähnlichen Gründen werden gelegentlich Zeilen in die Buch-Schnipsel eingefügt, die tatsächlich gar nicht ausgeführt werden (Kommentar `#!` am Beginn der Zeile). Das ist zum Beispiel sinnvoll, um Code darzustellen, der zu bestimmten Fehlern führt.


## Begleitmaterial interaktiv ausprobieren

Um erste Erfahrungen mit dem Quellcode zu sammeln, bietet sich die Browser-basierte Lösung *Binder* an. Dabei handelt es sich um einen Dienst, bei dem je nach Bedarf (durch Klick auf einen Link) eine virtuelle Maschine (VM) gestartet wird, auf der dann der Notebook-Server mit dem Inhalt des entsprechenden Repos läuft. Das Hochfahren der VM dauert ca. 2 min.  Danach erscheint der Inhalt des Verzeichnisses `notebooks` in einer Art Datei-Browser. Um zum ausführbaren Code zu gelangen, klicken Sie z.&#x202F;B. auf `kapitel_01_erstkontakt` und dann auf `erstkontakt.ipynb`. Das entsprechende Notebook öffnet sich in einem neuen Tab, sodass der Datei-Browser-Tab erhalten bleibt. Dadurch ist es einfach, mehrere Notebooks parallel laufen zu lassen. Im Notebook können Sie nun den Quellcode direkt ausführen (`Shift+Enter` in jeder Zelle, Details in Buch-Kapitel 1). Weiterhin hilfreich: *Help* → *User Interface Tour* und *Help* → *Keyboard Shortcuts*.

Hier geht's nun zum Notebook-Server auf einer eigens für Sie gestarteten Binder-VM: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/python-fuer-ingenieure/material/main?urlpath=/tree/notebooks).

Wenn Sie über die Kennenlernphase hinaus sind, empfehlen wir übrigens, sich Python und die relevante Zusatzsoftware lokal auf Ihrem Rechner zu installieren. Näheres dazu in Buch-Kapitel 2.

## Links zum Anklicken

Sparen Sie sich das Abtippen; alle Links im Buch sind hier noch einmal zum Anklicken aufgelistet.

- Kapitel 2: *Installation*
    - https://www.python.org/downloads/ - Downloads des Python-Interpreters
    - https://www.anaconda.com/products/individual - Downloads der *Anaconda*-Distribution
    - https://pypi.org/ - Python Package Index
    - https://www.spyder-ide.org/ - IDE *Spyder*
    - https://www.jetbrains.com/de-de/pycharm/ - IDE *PyCharm*
- Kapitel 3: *Grundlagen*
    - https://docs.python.org/3/library/string.html#formatspec - Details zur Stringformatierung
- Kapitel 4: *Effiziente Numerik mit NumPy*
    - https://numpy.org/doc/stable/user/basics.broadcasting.html - Dokumentation zum Broadcasting
    - https://numpy.org/devdocs/reference/arrays.indexing.html - Die fabelhafte Welt der Array-Indizierung
    - https://numpy.org/doc/stable/reference/routines.math.html - Mathematische Funktionen
    - https://numpy.org/doc/stable/user/numpy-for-matlab-users.html - *NumPy* für *Matlab*-Benutzer
- Kapitel 6: *Brunfzeit für Termhirsche*
    - https://docs.sympy.org/ - Dokumentation zu *SymPy*
- Kapitel 7: *Visualisierung*
    - https://matplotlib.org/ - Dokumentation zu *Matplotlib*
- Kapitel 8: *So tun, als ob: Modellbildung und Simulation*
    - https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html - Dokumentation zur Funktion `solve_ivp`
- Kapitel 9: *Optimierung - Besser geht's nicht*
    - https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html - Dokumentation zur Funktion `minimize`
    - https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html - Dokumentation zur Funktion `curve_fit`
    - https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html - Dokumentation zur Funktion `polyfit`
    - https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.UnivariateSpline.html - Details zu Splines in *NumPy*
- Kapitel 10: *Mechanik - Ganz ohne schmutzige Hände*
    - https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html - Dokumentation zur Funktion `fmin`
- Kapitel 12: *Kombinatorik, Zufall und Statistik*
    - https://de.wikipedia.org/wiki/Kombination_(Kombinatorik) - Gedankenexperiment zur Kombination mit Wiederholung
    - https://numpy.org/doc/stable/reference/random/generator.html#distributions - Wahrscheinlichkeitsverteilungen in *NumPy*
    - https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html - Tutorial zu Statistik mit *SciPy*
    - *Matplotlib*-Funktionen zum Visualisieren von Fehlern und Unsicherheiten
        - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html
        - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill_between.html
        - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html
        - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.violinplot.html
- Kapitel 13: *Python im Labor – Steuern, Messen, Filtern, Darstellen*
    - https://pyserial.readthedocs.io - Dokumentation zu *pySerial*
    - https://pyvisa.readthedocs.io - Dokumentation zu *pyVISA*
    - https://docs.python.org/3/library/socket.html - Dokumentation zu Sockets in der Standardbibliothek
    - https://docs.python.org/3/library/ctypes.html - Mit *ctypes* C-Code aufrufen
    - https://docs.python.org/3/library/logging.html - Dokumentation zum Logging
    - https://docs.scipy.org/doc/scipy/reference/signal.html#filtering - Signalfilterung mit *SciPy*
- Kapitel 15: *Profiling und Performanz-Optimierung*
    - https://www.thecodeship.com/patterns/guide-to-python-function-decorators/ - Überblick zu Dekoratoren
- Kapitel 16: *Von den Profis lernen - Das Wichtigste zur Softwaretechnik*
    - https://docs.python.org/3/library/unittest.html - Unittests mit Bordmitteln
    - https://ipython.readthedocs.io/en/stable/ - Dokumentation zu *IPython*
    - https://www.python.org/dev/peps/pep-0008/ - Konventionen zum Formatieren von Python-Code
    - https://git-scm.com/ - Versionsverwaltungssoftware *Git*
- Kapitel 17: *Die 10 nützlichsten Module, die bisher nicht erwähnt wurden*
    - https://riverbankcomputing.com/software/pyqt - GUIs mit *PyQt*
    - https://docs.python.org/3/library/re.html - Details zu regulären Ausdrücken
    - https://scikit-learn.org/stable/user_guide.html} - Dokumentation zu *Scikit-learn*
- Kapitel 18: *10 fiese Fallstricke und 3 Mal schwarze Python-Magie*
    - https://docs.python.org/3/library/2to3.html - Automatische Konversion von Python 2 zu Python 3
- Kapitel 19: *10 nützliche Links*
    - https://docs.python.org/3/tutorial/index.html - Offizielle Python-Dokumentation
    - https://docs.python.org/3/library/index.html - Dokumentation der Standardbibliothek
    - https://pypi.org/ - Python Package Index
    - https://book.pythontips.com/ - Nützliche fortgeschrittene Tipps zur Inspiration
    - https://github.com/search?l=Python&q=solve_ivp&type=Code - Suche nach Code auf *GitHub*
    - https://gitlab.com - Git-Host *GitLab.com*
    - https://codeberg.org - Git-Host *Codeberg*
    - https://pythex.org/ - Debugging von regulären Ausdrücken
    - https://regex101.com/ - Debugging von regulären Ausdrücken mit mehr Funktionen
    - https://computers-are-fast.github.io/ - Quiz zur Geschwindigkeit von Computern
    - https://stackoverflow.com/questions/tagged/sympy+matrix - Beispielsuche auf *Stack Overflow*
    - https://www.sphinx-doc.org/en/master/usage/quickstart.html - Dokumentationswerkzeug *Sphinx*
    - https://www.hackerrank.com/domains/python/numpy - Programmieraufgaben zu *NumPy*
    - https://edabit.com/challenges/python3 - Übungsaufgaben zum Selbstprogrammieren
    - https://cscircles.cemc.uwaterloo.ca/visualize - Schrittweises Ausführen von Python-Programmen - mit Zurückspulen
    - https://planet.scipy.org/ - Blogbeiträge zu *SciPy* und *NumPy*
    - https://planet.sympy.org/index.html - Blogbeiträge zu *SymPy*
    - https://planetpython.org/ - Blogbeiträge zu Python im Allgemeinen

## Fehler und Verbesserungsvorschläge melden

Auch wenn wir uns bei der Aufbereitung des Materials große Mühe gegeben haben, ist es unrealistisch anzunehmen, dass der Buch-Text und der Code keine Fehler enthalten. Wir bitten deshalb um eine E-Mail an die Autoren (`<vorname>.<nachname>@tu-dresden.de`) oder um das Öffnen eines [GitHub-Issues](https://github.com/python-fuer-ingenieure/begleitmaterial/issues). Das Gleiche gilt für allgemeine Kritik und Verbesserungsvorschläge zum Buch. Vielen Dank!


## Lizenz

Cover-Bild, Logos, Markennamen und sonstige Inhalte dieses Repos sind urheberrechtlich geschützt. Für Verwendungen, die nicht vom Zitatrecht gedeckt sind, wenden Sie sich an den Verlag oder die Autoren.
