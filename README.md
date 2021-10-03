# Python für Ingenieure für Dummies

Dieses Repo enthält das Begleitmaterial für das Buch **[Python für Ingenieure für Dummies](https://www.wiley-vch.de/de?option=com_eshop&view=product&isbn=9783527717675)**, erschienen im Wiley-VCH Verlag, 2021. Inhaltsverzeichnis, Probekapitel und Index sind auf der [Verlags-Website](https://www.wiley-vch.de/de?option=com_eshop&view=product&isbn=9783527717675) abrufbar.


[<img src="img/cover_book.png" title="Python für Ingenieure für Dummies" alt="Cover: Python für Ingenieure für Dummies" width="300">](https://www.wiley-vch.de/de?option=com_eshop&view=product&isbn=9783527717675)


## Zusammenhang zwischen Begleitmaterial und Buch

Alle Code-Beispiele ("Schnipsel") im Buch sind kapitelweise in Jupyer-Notebooks hinterlegt und können auf diese Weise direkt (ohne abtippen) ausgeführt werden. Viele der Beispiele erzeugen eine grafische Ausgabe die direkt der jeweiligen Abbildung im Buch entspricht. Damit ist die **Reproduzierbarkeit** der Ergebnisse gewährleistet.

Die Schnipsel im Buch wurden aus den Notebooks mit einem Skript erzeugt. Alle Code-Zeilen zwischen speziellen Markdown-Zellen (`begin XYZ` und `end`) werden zu einem Schnipsel für das Buch zusammengefasst – bis auf die Zeilen, die mit  dem speziellen Kommentar `#!` enden. Diese werden aus didaktischen Gründen ausgespart. Aus ähnlichen Gründen werden gelegentlich Zeilen in die Buch-Schnipsel eingefügt, die tatsächlich gar nicht ausgeführt werden (Kommentar `#!` am Beginn der Zeile). Das ist zum Beispiel sinnvoll, um Code darzustellen, der zu bestimmten Fehlern führt.


## Begleitmaterial interaktiv ausprobieren

Um erste Erfahrungen mit dem Quellcode zu sammeln, bietet sich die Browse-basierte Lösung *Binder* an. Dabei handelt es sich um einen Dienst, bei dem je nach Bedarf (durch Klick auf einen Link) eine virtuelle Maschine (VM) gestartet wird, auf der dann der Notebook-Server mit dem Inhalt des enstprechenden Repos läuft. Das Hochfahren der VM dauert ca. 2min und dann können Sie im Verzeichnis `notebooks` den Quellcode direkt ausführen (SHIFT+Enter in jeder Zelle, Details in Kapitel 1).

Hier geht's nun zum Notebook-Server auf einer eigens für Sie gestarteten VM: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/python-fuer-ingenieure/material/main). Denn ausführbaren Quellcode finden Sie dann nach Kapitel sortiert im Verzeichnis `notebooks`. Der beste Startpunkt ist `kapitel_01_erstkontakt`.

Wenn Sie über die Kennenlernphase hinaus sind, empfehlen wir übrigens sich Python und die relevante Zussatzsoftware lokal auf Ihrem Rechner zu installieren. Näheres dazu in Kapitel 2.

## Fehler und Verbesserungsvorschläge melden

Auch wenn wir uns bei der Aufbereitung des Materials große Mühe gegeben haben, ist es unrealistisch anzunehmen, dass der Buch-Text und der Code keine Fehler enthalten. Wir bitten deshalb um eine E-Mail an die Autoren (`<vorname>.<nachname>@tu-dresden.de`) oder um das Öffnen eines [Github-Issues](https://github.com/python-fuer-ingenieure/begleitmaterial/issues). Das Gleiche gilt für allgemeine Kritik und Verbesserungsvorschläge zum Buch. Vielen Dank!


## Lizenz

Cover-Bild, Logos, Markennamen und sonstige Inhalte dieses Repos sind urheberrechtlich geschützt. Für Verwendungen, die nicht vom Zitatrecht gedeckt sind, wenden Sie sich an den Verlag oder die Autoren.
