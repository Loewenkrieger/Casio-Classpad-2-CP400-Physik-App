# Physik LK v1.0.0 fuer Casio ClassPad II

Produktionsversion der Physik-Lernapp fuer PythonExtra unter Hollyhock 2.
146 Theorieartikel, 368 eindeutige Formeln, 514 einzeln ladbare Wissenskapitel
und 167 Rechner-/Messreihenfunktionen. Quanten- und Atomphysik ergaenzen
Mechanik, Schwingungen, Elektrizitaet und Wechselstrom.

## Download

Die fertigen oeffentlichen Pakete stehen im
[GitHub-Release v1.0.0](https://github.com/Loewenkrieger/Casio-Classpad-2-CP400-Physik-App/releases/tag/v1.0.0):

- `physik_classpad_v1_0_0.zip`: fuer den Taschenrechner.
- `physik_pc_v1_0_0.zip`: Vorschau fuer Windows mit installiertem Python 3
  einschliesslich Tkinter. `start_pc_preview.bat` startet die Vorschau.

Fuer den ClassPad das benannte ClassPad-Paket verwenden, nicht GitHubs
automatisches `Source code (zip)`: Dessen Entpackordner enthaelt Bindestriche
und eignet sich deshalb nicht als PythonExtra-Startpfad.

Das oeffentliche Paket enthaelt 39 eigene fachliche Abbildungen. Eine nur
lokal bereitgestellte private Variante ergaenzt acht Unterrichtsausschnitte
aus PDFs. Diese privaten Medien und Pakete werden nicht veroeffentlicht.

## Hollyhock 2 Und PythonExtra

Hollyhock 2 ist ein Community-Launcher und kein offizielles Casio-Produkt.
Eine Installation veraendert das Geraet und kann bei inkompatibler Hardware
zu Problemen fuehren. Zuerst die Kompatibilitaet in der
[Originalanleitung von Hollyhock 2](https://github.com/SnailMath/hollyhock-2#compatibility)
pruefen. Die dortigen Warnungen und Installationsschritte sind massgeblich.

1. Bei kompatiblem Geraet den vorbereiteten
   [Hollyhock-2-Release](https://github.com/SnailMath/hollyhock-2/releases)
   nach dessen Anleitung installieren. Updates nicht unterbrechen.
2. PythonExtra in der fuer Hollyhock 2 vorgesehenen Variante herunterladen:
   [offizielle PythonExtra-Installation](https://classpaddev.github.io/wiki/python/installation-guide/).
3. `PythonExtra-hh2.bin` nach dieser Anleitung in den USB-Speicher neben den
   Hollyhock-Launcher kopieren, sicher auswerfen und im Launcher starten.

Hollyhock/PythonExtra werden nicht mit dieser App mitgeliefert. Falls beide
bereits funktionieren, ist keine Neuinstallation erforderlich.

## App Installieren Oder Aktualisieren

Alle drei Dateien aus dem ClassPad-ZIP gemeinsam in denselben Ordner kopieren:

```text
physchem_final.py
wissen.txt
bilder.dat
```

Zum Beispiel den Ordner `Python` oder `physik_classpad_v1_0_0` verwenden.
Im gesamten Startpfad keine Leerzeichen, Bindestriche oder Klammern benutzen.
Dateien nicht in `physchem_final (1).py` umbenennen: Die Dateiliste startet
ueber Python-Importnamen. Unterstriche sind geeignet.

Beim Update alle drei Dateien ersetzen und keine Versionen oder privaten und
oeffentlichen Pakete mischen. Die Bilddatei wurde fuer den Release um
Testbilder bereinigt und hat deshalb einen neuen Byteindex/Paketheader.
Anschliessend PythonExtra neu starten und `physchem_final.py` in der
Dateiliste auswaehlen.

Auf dem ClassPad werden **weder `cinput.py`, `gint.py` noch ein separater
Index** benoetigt. Die PC-Datei `gint.py` darf nicht auf das Geraet kopiert
werden, da sie dort das native Grafikmodul ueberschatten wuerde.

## Bedienung

Das Hauptmenue besteht aus Theorie, Formeln nach Groessen, Formeln nach
Themen, Physik-Rechner und Beenden. Touch und Pfeiltasten dienen der Auswahl
und Navigation; DEL/Zurueck fuehrt zur vorherigen Ansicht.

Artikel mit Bildern haben `Abbildungen (EXE)`. EXE oder der Touch-Button
oeffnet die Ansicht, links/rechts wechselt die Bilder, Zurueck stellt die
bisherige Textposition wieder her. Eigene Modelle und synthetische
Nachweismuster sind als solche gekennzeichnet.

Der Rechner nutzt fest programmierte Formeln statt `eval()` oder eines
freien Symbol-Solvers. Passende Einheiten wie nm/pm/m und eV/keV/J lassen
sich mit `Einheit` umschalten. Ein Messreihen-Assistent bestimmt unter
anderem h und die Austrittsarbeit aus zwei oder 3-10 Messpunkten.
Geltungsbedingungen und Hinweise stehen in den zugehoerigen Artikeln.

## Speicher Und Kompatibilitaet

Wissen und Verzeichnisse werden nach Bedarf aus den Begleitdateien gelesen,
nicht vollstaendig beim Start geladen. Bilder verwenden bytegenaues
`readinto()` und rohe RGB565-Paletten. Rasterbilder werden ohne
Verkleinerung in maximal 128 Zeilen hohen Abschnitten gezeichnet, um den
8-Bit-Zeilenueberlauf aelterer gint-Versionen zu umgehen.

Ein grosses Rasterbild benoetigt weiterhin rund 95 KiB Puffer. Zu wenig
Speicher oder fehlende/beschaedigte Dateien ergeben eine Fehlermeldung;
Theorie und Rechner bleiben bei einem reinen Medienfehler benutzbar.
Nach einem Fehler PythonExtra bei Bedarf neu starten und das komplette
zusammengehoerige Paket erneut uebertragen.

## Pruefstatus Und Hinweise

Der Nutzer hat Start, Skizzen, Rasterbilder und Bildnavigation des
zugrundeliegenden RAM-Builds auf seinem ClassPad bestaetigt. Gemeldet wurde
MicroPython `v1.25.0-preview.589.gd5d03e81b`, sh7305/sh-4a, vom 18.04.2025.
Die Produktionsbereinigung wird zusaetzlich am PC geprueft. Dies ist keine
Behauptung eines vollstaendigen Hardwaretests aller Funktionen oder einer
Freigabe fuer jede PythonExtra-/Geraeteversion. PC-RAM-Messungen sind keine
ClassPad-RAM-Werte.

Grafiktests, RAM-Messfenster nach Artikeln und Debug-Ausgaben sind nicht
Bestandteil des Produktionsprogramms. Die Entwicklungsfassung bleibt lokal
mit ihren Diagnosewerkzeugen erhalten.

Dieses Community-Projekt ist nicht mit Casio verbunden. Schul- und
Pruefungsregeln beachten; keine Zusicherung fuer den Pruefungsmodus.
Installationsquellen zuletzt am 27.10.2026 geprueft.
