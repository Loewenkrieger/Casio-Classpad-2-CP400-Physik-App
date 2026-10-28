# Physik LK On-Demand für den Casio ClassPad II

> [!IMPORTANT]
> Diese Projektlinie ist für **Hollyhock 2** vorgesehen. Zuverlässiger Betrieb
> unter Hollyhock 3 wird nicht zugesichert; insbesondere sind dort stark
> verlängerte Bildladezeiten bekannt. Die HH3-Weiterentwicklung erfolgt
> separat in einem privaten Projekt. Diese Projektlinie bleibt bei HH2.

Eine kompakte Physik-Lernapp für den Casio ClassPad II. Sie enthält
Theorieartikel, Formelsammlungen, einen Physik-Rechner und passende
Abbildungen für den Physik-Leistungskurs.

Die App läuft mit **PythonExtra** über den Community-Launcher
**Hollyhock 2**. Die aktuelle Produktionsversion ist **v1.0.0**.

> [!WARNING]
> Hollyhock 2 verändert die Firmware des ClassPads. Die Installation erfolgt
> auf eigene Gefahr und kann bei inkompatiblen Geräten zu einem schwarzen
> Bildschirm führen. Prüfe vor der Installation die Kompatibilität deines
> Geräts in der [offiziellen Hollyhock-2-Anleitung](https://github.com/SnailMath/hollyhock-2#compatibility).

## Funktionen

- Theorie nach Themengebieten sowie Formeln nach physikalischen Größen und Themen.
- **146 Theorieartikel**, **368 eindeutige Formeln** und **514 Wissenskapitel**.
- **167 Rechner- und Messreihenfunktionen** mit passenden Einheiten.
- Mechanik, Schwingungen, Elektrizität und Wechselstrom sowie Quanten- und Atomphysik.
- **39 eigene fachliche Abbildungen**, direkt aus den passenden Artikeln erreichbar.
- Lädt Wissen, Verzeichnisse und Bilder nur bei Bedarf, statt alles beim Start einzulesen.
- Für den begrenzten Arbeitsspeicher des ClassPads optimiert.

## Download

Die fertigen Pakete findest du im
[GitHub-Release v1.0.0](https://github.com/Loewenkrieger/Casio-Classpad-2-CP400-Physik-App/releases/tag/v1.0.0):

| Paket | Verwendung |
| --- | --- |
| [physik_classpad_v1_0_0.zip](https://github.com/Loewenkrieger/Casio-Classpad-2-CP400-Physik-App/releases/download/v1.0.0/physik_classpad_v1_0_0.zip) | Fertige App für den Taschenrechner |
| [physik_pc_v1_0_0.zip](https://github.com/Loewenkrieger/Casio-Classpad-2-CP400-Physik-App/releases/download/v1.0.0/physik_pc_v1_0_0.zip) | PC-Vorschau für Windows mit Python 3 und Tkinter |

> [!IMPORTANT]
> Verwende für den ClassPad das benannte ClassPad-Paket, nicht GitHubs
> automatisches `Source code (zip)`. Dessen Entpackordner enthält Bindestriche
> und eignet sich deshalb nicht als PythonExtra-Startpfad.

Das öffentliche Paket enthält ausschließlich eigene fachliche Abbildungen.
Eine getrennte private Variante ergänzt acht Unterrichtsausschnitte aus
PDFs. Diese privaten Medien und Pakete werden nicht auf GitHub veröffentlicht.

## Benötigte Dateien

Auf dem ClassPad werden genau diese drei App-Dateien benötigt:

```text
physchem_final.py
wissen.txt
bilder.dat
```

| Datei | Inhalt |
| --- | --- |
| `physchem_final.py` | Oberfläche, Navigation und Physik-Rechner |
| `wissen.txt` | Theorie, Formeln und nach Bedarf geladene Verzeichnisse |
| `bilder.dat` | Fachliche Skizzen und Rasterbilder |

Alle drei Dateien müssen **im selben Ordner** liegen und zur selben
Paketversion gehören.

**Zusätzliche Dateien wie `cinput.py`, `gint.py` oder eine separate
Indexdatei werden nicht benötigt.** Die `gint.py` aus der PC-Vorschau gehört nicht auf den
ClassPad: Dort würde sie das native Grafikmodul überlagern.

## 1. Hollyhock 2 installieren

### Kompatibilität prüfen

Die [Hollyhock-2-Projektseite](https://github.com/SnailMath/hollyhock-2#compatibility)
nennt den `fx-CP400`, `fx-CP400+E` und `fx-CG500`, warnt aber vor neueren
Hardware-Revisionen. Ein passender Modellname allein reicht deshalb nicht.
Installiere Hollyhock 2 nicht auf einem inkompatiblen oder ungeklärten Gerät.

### Installation zusammengefasst

1. Prüfe dein Gerät anhand der Kompatibilitätsprüfung der Projektseite.
2. Lade einen vorbereiteten
   [Hollyhock-2-Release](https://github.com/SnailMath/hollyhock-2/releases) herunter.
3. Entpacke den enthaltenen Ordner `Snail2021` auf den Windows-Desktop.
4. Starte `Snail2021.exe` und folge der Originalanleitung. Verbinde den
   ClassPad erst, wenn du dazu aufgefordert wirst.
5. Unterbrich das Firmware-Update nicht. Kopiere anschließend die in der
   Anleitung genannten Launcher-Dateien, einschließlich `run.bin`, in das
   Hauptverzeichnis des ClassPad-Speichers und wirf das Gerät sicher aus.

Die ausführliche Originalanleitung und ihre Warnhinweise sind maßgeblich.
Wenn Hollyhock 2 bereits funktioniert, ist keine Neuinstallation nötig.

## 2. PythonExtra installieren

PythonExtra stellt die Python-Umgebung für die App bereit.

1. Lade die zu Hollyhock 2 passende Datei `PythonExtra-hh2.bin` von der
   [offiziellen PythonExtra-Downloadseite](https://classpaddev.github.io/python/#download) herunter.
2. Verbinde den ClassPad per USB und wähle den USB-Massenspeicher, falls
   danach gefragt wird.
3. Kopiere `PythonExtra-hh2.bin` in das Hauptverzeichnis des
   ClassPad-Speichers, direkt neben `run.bin`.
4. Wirf das Gerät sicher aus und öffne den Hollyhock-Launcher über das
   Systemmenü des ClassPads.
5. Wähle `PythonExtra` aus und starte es.

Weitere Informationen stehen in der
[offiziellen PythonExtra-Installationsanleitung](https://classpaddev.github.io/wiki/python/installation-guide/).
Hollyhock und PythonExtra werden nicht mit dieser App mitgeliefert.

## 3. Physik-App installieren oder aktualisieren

1. Lade `physik_classpad_v1_0_0.zip` aus dem Release herunter und entpacke es.
2. Verbinde den ClassPad per USB mit dem Computer.
3. Kopiere `physchem_final.py`, `wissen.txt` und `bilder.dat` gemeinsam in
   denselben Ordner, beispielsweise `Python` oder `physik_classpad_v1_0_0`.
4. Wirf das Gerät sicher aus und starte PythonExtra neu.
5. Wähle `physchem_final.py` in der Dateiliste aus und starte die App.

> [!IMPORTANT]
> Verwende im gesamten Startpfad keine Leerzeichen, Bindestriche oder Klammern.
> Unterstriche sind geeignet. Ein Name wie `physchem_final (1).py` oder ein
> Ordner wie `classpad-testpaket` kann beim Start einen `SyntaxError` auslösen,
> weil die Dateiliste Python-Importnamen verwendet.

Bei einem Update **immer alle drei Dateien gemeinsam ersetzen**. Mische
weder unterschiedliche Versionen noch private und öffentliche Pakete.
Die Bilddatei von v1.0.0 wurde um Testbilder bereinigt und besitzt einen
neuen Byteindex und Paketheader.

## 4. PC-Vorschau starten

1. Entpacke `physik_pc_v1_0_0.zip` in einen eigenen Ordner auf dem PC.
2. Stelle sicher, dass Python 3 einschließlich Tkinter installiert ist.
3. Starte `start_pc_preview.bat`.

Die PC-Vorschau enthält ihre eigene Grafiksimulation `gint.py`. Diese Datei
wird nur am PC benötigt und darf nicht auf den Taschenrechner kopiert werden.

## Bedienung

Das Hauptmenü enthält ausschließlich:

| Menüpunkt | Funktion |
| --- | --- |
| Theorie | Wissen nach Themengebieten lesen |
| Formeln nach Groessen | Formeln über die gesuchte physikalische Größe finden |
| Formeln nach Themen | Formeln nach Themengebieten durchsuchen |
| Physik-Rechner | Formel auswählen, Werte eingeben und Ergebnis berechnen |
| Beenden | Die App schließen |

- Ein Thema antippen oder mit den Pfeiltasten auswählen.
- Mit Pfeiltasten beziehungsweise Touchscreen scrollen.
- Mit DEL beziehungsweise Zurück zur vorherigen Ansicht wechseln.
- In Artikeln mit Bildern `Abbildungen (EXE)` antippen oder EXE drücken.
- Mit links/rechts zwischen den Abbildungen wechseln. Zurück führt zur
  bisherigen Textposition.

Der Rechner verwendet feste Formeln statt eines freien Symbol-Solvers.
Über `Einheit` lassen sich passende Einheiten wie nm/pm/m oder eV/keV/J
auswählen. Der Messreihen-Assistent bestimmt unter anderem das Plancksche
Wirkungsquantum und die Austrittsarbeit aus zwei oder 3–10 Messpunkten.
Gültigkeitsbedingungen stehen in den zugehörigen Artikeln.

Grafiktests, Debug-Ausgaben und RAM-Messfenster nach Artikeln sind **nicht**
Bestandteil der Produktionsversion.

## Quanten- und Atomphysik

Die Erweiterung behandelt Photonen und Photoeffekt, Materiewellen und
Beugung, Superposition und Messung, Verschränkung und Quantenradierer sowie
Unbestimmtheit und Wellenpakete. Hinzu kommen Potentialtopf, Atommodelle,
Orbitale, Spektren, Franck-Hertz, Lumineszenz, Laser und Röntgenstrahlung.

Die 32 neuen Theorieartikel besitzen passende Abbildungen. Eigene Modelle
und synthetische Nachweismuster sind als solche gekennzeichnet; sie werden
nicht als Originalmessungen oder tatsächliche Elektronenbahnen ausgegeben.

## Wie das On-Demand-Wissen funktioniert

Die App findet Kapitel über Bytepositionen und Längen in `wissen.txt`.
Beim Öffnen eines Themas wird nur der angeforderte Textabschnitt gelesen.
Auch die Verzeichnisse werden erst bei Bedarf geladen. Die gesamte
Wissensdatei muss dadurch nicht gleichzeitig im Arbeitsspeicher liegen.

Für Abbildungen wird jeweils nur eine Darstellung aus `bilder.dat` geladen.
Die Dateien müssen zusammenpassen, weil ihre Paketkennungen und Positionen
aufeinander abgestimmt sind. Große `seek()`-Sprünge werden vermieden, da sie
auf dem ClassPad Probleme verursachen können.

### Technische Hinweise

Binärdaten werden bytegenau mit `readinto()` eingelesen. Rasterbilder nutzen
rohe RGB565-Paletten und werden ohne Verkleinerung in höchstens 128 Zeilen
hohen Abschnitten gezeichnet. Das umgeht einen Zeilenüberlauf älterer
gint-Versionen und erhält das vollständige Bild.

Ein großes Rasterbild benötigt weiterhin ungefähr 95 KiB Puffer.
PC-RAM-Messungen lassen sich nicht mit ClassPad-RAM-Werten gleichsetzen.

## Fehlerbehebung

### Die App startet mit `SyntaxError: invalid syntax`

Prüfe Ordner- und Dateinamen. Verwende beispielsweise `Python/physchem_final.py`
statt eines Ordners mit Bindestrich oder einer Datei mit dem Zusatz `(1)`.
Entpacke für das Gerät das benannte ClassPad-ZIP, nicht das automatische
Source-code-ZIP von GitHub.

### Eine Begleitdatei fehlt oder passt nicht zur App

Prüfe, ob `physchem_final.py`, `wissen.txt` und `bilder.dat` direkt
nebeneinander liegen und exakt so heißen. Ersetze bei Unsicherheit alle drei
Dateien aus demselben Paket und starte PythonExtra neu.

### Ein Bild fehlt, wird nicht vollständig angezeigt oder meldet einen Fehler

Übertrage das vollständige aktuelle Paket erneut, nicht nur die Python-Datei.
Bei einem reinen Medienfehler bleiben Theorie und Rechner benutzbar.
Wenn das Problem bestehen bleibt, notiere die angezeigte Fehlermeldung und
deine PythonExtra-Version.

### Es erscheint ein `MemoryError`

Starte PythonExtra neu, damit alter belegter Speicher freigegeben wird.
Prüfe außerdem, ob wirklich alle drei Dateien aus der aktuellen Version
verwendet werden. Notiere bei erneutem Auftreten den vollständigen Fehlertext
und ob der Fehler beim Start, beim Artikel oder beim Bild auftritt.

### PythonExtra erscheint nicht im Hollyhock-Launcher

Prüfe Dateiname und Ablageort von `PythonExtra-hh2.bin`. Die Datei muss für
Hollyhock 2 bestimmt sein und im Hauptverzeichnis neben `run.bin` liegen.
Weitere Schritte findest du in der verlinkten PythonExtra-Anleitung.

## Prüfstatus

Für v1.0.0 wurden **41 bestehende Regressionstestgruppen** und **7 zusätzliche
Produktionsprüfgruppen** erfolgreich ausgeführt. Alle Wissenskapitel,
Rechnerfunktionen und fachlichen Abbildungen wurden softwareseitig geprüft.
Zusätzlich wurden in beiden PC-Varianten jeweils 20 Bildwechsel getestet.
Die veröffentlichten ZIPs wurden erneut heruntergeladen und bytegenau mit
den geprüften lokalen Paketen verglichen.

Auf dem ClassPad wurden Start, Skizzen, Rasterbilder und Bildnavigation des
zugrunde liegenden Entwicklungsbuilds vom Nutzer bestätigt. Gemeldet wurde
MicroPython `v1.25.0-preview.589.gd5d03e81b`, sh7305/sh-4a, vom 18.04.2025.
Das ist **kein vollständiger Hardwaretest aller Funktionen der
Produktionsversion** und keine Freigabe für jede Geräte- oder PythonExtra-Version.

## Hinweise

- Dieses Projekt ist ein Community-Projekt und nicht mit Casio verbunden.
- Hollyhock und PythonExtra stammen von ihren jeweiligen Community-Projekten.
- Beachte die Regeln deiner Schule und die Prüfungsordnung. Eine Nutzung im
  Prüfungsmodus wird nicht zugesichert.
- Private PDF-Abbildungen bleiben außerhalb des öffentlichen Repositorys und
  der öffentlichen Downloads.
- Die Installationsquellen wurden zuletzt am **28. Oktober 2026** geprüft.
