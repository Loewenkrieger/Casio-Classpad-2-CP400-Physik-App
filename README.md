# Physik LK On-Demand für den Casio ClassPad II

Eine kompakte Physik-Lernapp für den Casio ClassPad II. Sie enthält
Theorieartikel und Formelsammlungen für den Physik-Leistungskurs.

Die App läuft mit **PythonExtra** über den Community-Launcher
**Hollyhock 2**.

> [!WARNING]
> Hollyhock 2 verändert die Firmware des ClassPads. Die Installation erfolgt
> auf eigene Gefahr und kann bei inkompatiblen Geräten zu einem schwarzen
> Bildschirm führen. Prüfe unbedingt zuerst die Kompatibilität deines Geräts
> in der offiziellen Hollyhock-2-Anleitung.

## Funktionen

- Theorie nach Themengebieten
- Formeln nach physikalischen Größen
- Formeln nach Themengebieten
- 92 Theorieartikel und 215 eindeutige Formeln
- 307 Wissenskapitel mit 522 Navigationseinträgen
- Lädt nur das aktuell geöffnete Kapitel aus `wissen.txt`
- Für den begrenzten Arbeitsspeicher des ClassPads optimiert

## Benötigte Dateien

Für die App werden nur diese beiden Dateien benötigt:

```text
physchem_final.py
wissen.txt
```

Beide Dateien müssen auf dem ClassPad direkt nebeneinander liegen.

Benötigte Community Add-On's die ihr auf classpad.dev findet:
- Cinput welches ein Python Skript ist was auch im selben Ordner sitzt neben pyschem_final.py und wissen.txt

## 1. Hollyhock 2 installieren

Hollyhock 2 ist ein Community-Launcher für native Programme auf dem
ClassPad II.


### Kompatibilität prüfen

Hollyhock 2 unterstützt laut Projektseite den `fx-CP400`, `fx-CP400+E` und
`fx-CG500`, aber nicht jede Hardware-Revision.

Neuere Geräte mit `ABS_Date 2022/10/28 13:16` sind nicht mit Hollyhock 2
kompatibel. Auf diesen Geräten können ältere Betriebssystemversionen zu einem
schwarzen Bildschirm führen. Verwende Hollyhock 2 nicht, wenn dein Gerät laut
Projektseite inkompatibel oder unbekannt ist.

Die vollständige Kompatibilitätsprüfung und Warnhinweise stehen hier:

- [Hollyhock-2-Projekt und Installationsanleitung](https://github.com/SnailMath/hollyhock-2#compatibility)
- [Hollyhock-2-Releases](https://github.com/SnailMath/hollyhock-2/releases)

### Installation zusammengefasst

1. Prüfe zuerst die Kompatibilität deines ClassPads.
2. Lade den neuesten vorbereiteten Hollyhock-2-Release herunter.
3. Entpacke den enthaltenen Ordner `Snail2021` auf dem Windows-Desktop.
4. Starte `Snail2021.exe` und folge exakt den angezeigten Anweisungen.
5. Schließe den ClassPad erst an, wenn das Installationsprogramm dazu
   auffordert.
6. Berühre oder trenne den ClassPad während des Firmware-Updates nicht.
7. Kopiere anschließend `run.bin` und die benötigten Hollyhock-Programme in
   das Hauptverzeichnis des ClassPad-Speichers.
8. Wirf den ClassPad sicher aus.

Die ausführliche Originalanleitung ist maßgeblich. Bei Unsicherheit sollte die
Installation nicht durchgeführt werden.


## 2. PythonExtra installieren

PythonExtra stellt die Python-Umgebung bereit, in der diese App läuft.

1. Lade für Hollyhock 2 die Datei `PythonExtra-hh2.bin` herunter:
   [PythonExtra für ClassPad II](https://classpaddev.github.io/python/#download)
2. Verbinde den ClassPad per USB mit dem Computer.
3. Wähle am ClassPad den USB-Massenspeicher, falls danach gefragt wird.
4. Kopiere `PythonExtra-hh2.bin` in das Hauptverzeichnis des
   ClassPad-Speichers, direkt neben `run.bin`.
5. Wirf den ClassPad sicher aus.
6. Öffne auf dem ClassPad das Systemmenü und anschließend den
   Hollyhock-Launcher.
7. Wähle `PythonExtra` aus und starte es mit `Run`.

Weitere Informationen:

- [Offizielle PythonExtra-Installationsanleitung](https://classpaddev.github.io/wiki/python/installation-guide/)
- [PythonExtra-Quellcode](https://github.com/TheRainbowPhoenix/PythonExtra)

## 3. Physik-App installieren

1. Verbinde den ClassPad erneut per USB mit dem Computer.
2. Kopiere `physchem_final.py` und `wissen.txt` in denselben Ordner auf dem
   ClassPad, beispielsweise in den Ordner `Python`.
3. Wirf den ClassPad sicher aus.
4. Starte PythonExtra über den Hollyhock-Launcher.
5. Öffne und starte `physchem_final.py`.

Es werden keine zusätzliche `cinput.py`, `gint.py` oder
`knowledge_index.py` benötigt.

## 4. Cinput installieren

1. Ladet von classpad.dev das Cinput Skript herunter und packt es neben die anderen Dateien.

## Bedienung

- Ein Thema antippen oder auswählen, um es zu öffnen.
- Mit den Pfeiltasten beziehungsweise dem Touchscreen scrollen.
- Mit der Zurück-Taste zur vorherigen Auswahl zurückkehren.

Nach dem Schließen eines Artikels zeigt die App Messwerte zum freien
Arbeitsspeicher an. Diese dienen der Entwicklung und Optimierung.

## Wie das On-Demand-Wissen funktioniert

Der Byteindex ist direkt in `physchem_final.py` eingebettet. Für jedes Kapitel
kennt die App dessen Startposition und Länge in `wissen.txt`.

Beim Öffnen eines Themas wird nur der zugehörige Textabschnitt eingelesen.
Die gesamte Wissensdatei muss dadurch nicht gleichzeitig im Arbeitsspeicher
liegen. Der Loader vermeidet außerdem große `seek()`-Sprünge, da diese bei
PythonExtra auf dem ClassPad Fehler verursachen können.

## Fehlerbehebung

### `wissen.txt fehlt neben physchem_final.py`

Prüfe, ob `physchem_final.py` und `wissen.txt` wirklich im selben Ordner
liegen und exakt so benannt sind.

### PythonExtra erscheint nicht im Hollyhock-Launcher

Prüfe, ob `PythonExtra-hh2.bin` im Hauptverzeichnis direkt neben `run.bin`
liegt und ob Hollyhock 2 korrekt installiert wurde.

### Der ClassPad friert beim Start von PythonExtra ein

Setze das Gerät zurück und prüfe Dateiname, Hollyhock-Version und
Kompatibilität. Nutze bei Unsicherheit die
[ClassPadDev-Community](https://discord.gg/knpcNJTzpd).

## Hinweise

- Dieses Projekt ist ein Community-Projekt und nicht mit Casio verbunden.
- Hollyhock und PythonExtra stammen von ihren jeweiligen Community-Projekten.
- Beachte die Regeln deiner Schule und Prüfungsordnung.
- Die Installationslinks wurden zuletzt am **11. Juni 2026** geprüft.
