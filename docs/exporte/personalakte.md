---
title: Personalakte Export
description: "Personalakte Export im arkivado CONNECTOR: Entgeltunterlagen nach § 8 BVV aus ecoDMS prüfungsfertig für die Betriebsprüfung der Deutschen Rentenversicherung exportieren."
tags:
    - Personalakte
    - DRV
    - Betriebsprüfung
    - BVV
    - ecoDMS
    - Export
---

# Personalakte Export

Bei einer Betriebsprüfung fordert die Deutsche Rentenversicherung (DRV) die Entgeltunterlagen
der Beschäftigten an. Der **Personalakte Export** stellt diese Unterlagen aus ecoDMS
zusammen, so wie die DRV sie erwartet:

- je Beschäftigtem ein eigener Ordner
- je Unterlage eine Datei mit DRV-konformem Dateinamen
- ein **Inhaltsverzeichnis**, das jede Datei dem Beschäftigten zuordnet
- ein **Prüfbericht**, der zeigt, welche Unterlagen fehlen oder nachgebessert werden müssen

Grundlage sind § 8 der Beitragsverfahrensverordnung (BVV) und die Gemeinsamen Grundsätze
nach § 9a BVV.

!!! info "Voraussetzungen"
    - Gültige Lizenz mit dem Modul **Personalakte**. Ohne das Modul können Sie Definitionen
      ansehen, aber nicht exportieren.
    - Erreichbarer ecoDMS-Server
    - Ein ecoDMS-Feld mit der **Personalnummer** an den Personaldokumenten
    - Benutzerrecht **Personalakte Export**: „Ausführen“ und/oder „Konfigurieren“

---

## Ergebnis eines Exports

Jeder Lauf legt im Zielordner einen **neuen Ordner** an. Frühere Exporte werden nie
überschrieben.

```text
DRV-Pruefung_Muster_GmbH_2026-10-28_143005\
├── inhaltsverzeichnis.csv
├── pruefbericht.csv
├── 1001\
│   ├── befreiungsantrag_rv-1001-4711.pdf
│   └── niederschrift_nachweisgesetz-1001-4712.pdf
└── 1002\
    └── arbeitserlaubnis-1002-4801.pdf
```

| Datei | Inhalt |
| --- | --- |
| `inhaltsverzeichnis.csv` | Eine Zeile je exportierter Unterlage: Personalnummer, Unterlage, Datum, DocID, Ordner, Datei, Originaldatei und Prüfsumme (SHA-256) |
| `pruefbericht.csv` | Alle Fehler, Warnungen und Hinweise je Unterlage (siehe [Prüfbericht](#prufbericht)) |
| Ordner je Beschäftigtem | Die Unterlagen als einzelne Dateien |

Beide CSV-Dateien lassen sich direkt mit Excel öffnen.

!!! tip "Als ZIP-Datei packen"
    Ist **Als ZIP-Datei packen** gesetzt, entsteht statt des Ordners eine ZIP-Datei.
    Der Ordner wird danach gelöscht, damit keine zweite Kopie der Personaldaten
    liegen bleibt.

---

## Konfiguration

Auf der Registerkarte **Konfiguration** legen Sie beliebig viele Definitionen an, z. B. je
Firma eine. Jede Definition wird in fünf Schritten eingerichtet.

### Definitionen verwalten

- **Neue Definition** legt eine weitere Definition an.
- **Speichern** sichert alle Definitionen. Die Schaltfläche ist nur aktiv, wenn es
  Änderungen gibt.
- Der Schalter **Aktiv/Pausiert** steuert, ob die Definition bei
  **Alle aktiven exportieren** mitläuft. Pausierte Definitionen können Sie weiterhin
  einzeln exportieren.
- **Duplizieren** erzeugt eine Kopie, **Löschen** entfernt die Definition.

!!! warning "Erst speichern, dann exportieren"
    Solange eine Definition ungespeicherte Änderungen enthält, lässt sie sich nicht
    exportieren. Der CONNECTOR arbeitet immer mit dem gespeicherten Stand.

### 1. Welche Dokumente kommen grundsätzlich in Frage?

Der **Grundfilter** gilt für alle Unterlagenarten der Definition, z. B. die Firma, wenn in
ecoDMS mehrere Firmen liegen.

Darunter wählen Sie, ob alle passenden Unterlagen exportiert werden oder nur die aus einem
Zeitraum:

| Auswahl | Bedeutung |
| --- | --- |
| Alle passenden Unterlagen | Nur die Filter grenzen die Unterlagen ein |
| Nur aus einem Zeitraum | Zusätzlich nur Unterlagen aus einem Zeitraum, z. B. dem Prüfzeitraum der DRV |

Beim Zeitraum stellen Sie ein, ob er beim Exportieren abgefragt wird, dynamisch ist
(z. B. letztes Jahr) oder fest hinterlegt ist. Unter
**Zeitraum bezieht sich auf das Datumsfeld** wählen Sie das ecoDMS-Datumsfeld. Ohne
Auswahl gilt das globale Datumsfeld aus den Einstellungen.

### 2. Wie wird eine Unterlage dem Beschäftigten zugeordnet?

Wählen Sie das ecoDMS-Feld mit der **Personalnummer**. Sie ist das betriebliche
Ordnungsmerkmal nach § 8 Abs. 1 Satz 2 BVV und bestimmt, in welchem Ordner eine Unterlage
landet.

!!! danger "Pflichtfeld"
    Unterlagen, bei denen dieses Feld leer ist, werden **nicht exportiert**. Sie erscheinen
    im Prüfbericht als Fehler.

### 3. Welche Unterlagenarten gehören dazu?

Jede Unterlagenart hat eine **Bezeichnung** und einen eigenen **Filter**, z. B.
`Dokumentenart = Befreiungsantrag`. Die Bezeichnung erscheint später im Dateinamen.

- **Unterlagenart hinzufügen** legt eine leere Unterlagenart an.
- **Aus Katalog § 8 BVV** fügt eine Unterlagenart aus dem Katalog ein (siehe
  [Katalog](#katalog-der-unterlagen-nach-8-abs-2-bvv)). Bezeichnung und
  Unterschriftspflicht sind dann schon gesetzt, den Filter ergänzen Sie selbst.
- **Unterschriftspflichtig**: Ist die Unterlage nicht elektronisch signiert, weist der
  Prüfbericht darauf hin, das Papieroriginal aufzubewahren.

!!! note "Ein Dokument, eine Unterlagenart"
    Passt ein Dokument zu mehreren Unterlagenarten, wird es nur einmal exportiert, und zwar
    unter der **ersten** passenden Unterlagenart. Der Prüfbericht vermerkt das als Hinweis.

!!! danger "Filter ist Pflicht"
    Jede Unterlagenart braucht einen Filter, entweder einen eigenen oder den Grundfilter
    aus Schritt 1. Sonst bricht der Export mit einer Fehlermeldung ab. Damit wird
    verhindert, dass versehentlich das gesamte Archiv exportiert wird.

### 4. Wo und unter welchem Namen werden die Unterlagen abgelegt?

**Zielordner (lokal)**: Hier legt jeder Lauf seinen Ordner `<Name>_<Datum>_<Uhrzeit>` an.
Bleibt das Feld leer, wird der Unterordner `Personalakte` im Export-Pfad aus den
Einstellungen verwendet.

**Ordner je Beschäftigtem** und **Dateiname** setzen Sie aus Platzhaltern zusammen. Ziehen
Sie einen Platzhalter per Drag & Drop in das Eingabefeld oder klicken Sie ihn an.

| Platzhalter | Wert |
| --- | --- |
| `<@unterlage>` | Bezeichnung der Unterlagenart |
| `<@personalnummer>` | Wert aus dem Feld mit der Personalnummer |
| `<DocID>`, `<Dokumentenart>` | DocID bzw. Dokumentart aus ecoDMS |
| `<Feldname>` | Jedes weitere ecoDMS-Feld, z. B. `<Nachname>` oder `<Datum>` |

| Vorlage | Standard | Beispiel |
| --- | --- | --- |
| Ordner je Beschäftigtem | `<@personalnummer>` | `<@personalnummer>_<Nachname>` |
| Dateiname | `<@unterlage>-<@personalnummer>-<DocID>` | `<@unterlage>-<Nachname>_<Vorname>-<Datum>` |

Laut DRV soll der Dateiname die Art der Unterlage, den Namen und einen Zeitbezug enthalten.

!!! info "DRV-konforme Namen"
    Der CONNECTOR bildet alle Ordner- und Dateinamen automatisch nach den Vorgaben der DRV:

    - höchstens 64 Zeichen inklusive Dateiendung
    - nur Buchstaben, Ziffern, `-` und `_`; alle anderen Zeichen und Leerzeichen werden
      zu `_`
    - Umlaute werden umgeschrieben (ä → ae, ß → ss)
    - die Dateiendung wird anhand des Dateiinhalts ergänzt
    - gleiche Namen im selben Ordner erhalten `-2`, `-3` usw.

    Unter den Eingabefeldern zeigt ein Beispiel, wie Ordner und Dateiname aussehen werden.

### 5. Was soll danach in ecoDMS passieren? (optional)

Wie beim [Datei-Export](../dateien/konfiguration-dateiexport.md) kann der CONNECTOR das
Ergebnis nach ecoDMS zurückschreiben.

| Bereich | Einstellung | Bedeutung |
| --- | --- | --- |
| Aktion bei Erfolg | Feld-Aktionen | Felder, die bei exportierten Unterlagen gesetzt werden |
| | Export-Datum-Feld | Datumsfeld, das auf das aktuelle Datum gesetzt wird |
| Aktion bei Fehler | Feld-Aktionen | Felder, die bei nicht exportierten Unterlagen gesetzt werden, z. B. ohne Personalnummer oder mit unzulässigem Format |
| | Fehlertext-Feld | Textfeld für den Grund (max. 254 Zeichen) |

---

## Exportieren

Auf der Registerkarte **Ausführen** stehen alle Definitionen untereinander.

- **Exportieren** startet eine einzelne Definition.
- **Alle aktiven exportieren** startet alle aktiven Definitionen nacheinander.

Ist der Zeitraum auf „beim Exportieren abfragen“ eingestellt, öffnet sich vorher ein
Dialog zur Auswahl des Zeitraums.

Nach dem Lauf sehen Sie je Definition:

- eine Zusammenfassung, z. B. „12 Unterlagen exportiert, 2 nicht exportiert, 3 Warnungen“
- **Öffnen**, um den Ergebnisordner bzw. die ZIP-Datei zu öffnen
- die Meldungen aus dem Prüfbericht mit DocID; die vollständige Liste steht in
  `pruefbericht.csv`

### Prüfbericht

Jede Unterlage wird vor dem Export geprüft. Der Prüfbericht unterscheidet drei Stufen:

| Stufe | Bedeutung | Beispiele |
| --- | --- | --- |
| **Fehler** | Die Unterlage wurde **nicht exportiert** | Personalnummer leer · Format nicht zulässig · PDF passwortgeschützt oder defekt · Download aus ecoDMS fehlgeschlagen |
| **Warnung** | Exportiert, sollte aber geprüft werden | PDF enthält ausfüllbare Formularfelder, JavaScript, eingebettete Dateien oder Multimedia · PDF startet externe Programme oder lädt Inhalte nach · Schriften nicht eingebettet · Rückschreibung nach ecoDMS fehlgeschlagen |
| **Hinweis** | Zur Information | Unterschriftspflichtige Unterlage ohne elektronische Signatur: Papieroriginal aufbewahren · Dokument passt zu mehreren Unterlagenarten |

**Zulässige Formate** sind PDF, JPEG, BMP, PNG und TIFF. Das Format wird am Dateiinhalt
erkannt, nicht an der Dateiendung in ecoDMS.

!!! tip "Warnungen beheben"
    Die DRV verlangt PDFs, die nicht veränderbar sind und ihre Schriften eingebettet haben.
    Erzeugen Sie betroffene Dokumente z. B. als PDF/A neu, legen Sie sie in ecoDMS als neue
    Version ab und exportieren Sie erneut.

---

## Automatisch exportieren

In den [Cronjobs](../cronjobs.md) stehen zur Auswahl:

- **Personalakte Export: <Name>**: eine einzelne Definition
- **Personalakte Export: Alle Definitionen (ohne Zeitraum-Abfrage)**: alle aktiven
  Definitionen

!!! note ""
    Definitionen, die den Zeitraum beim Exportieren abfragen, können nicht zeitgesteuert
    laufen. Stellen Sie dafür einen dynamischen oder festen Zeitraum ein.

---

## Katalog der Unterlagen nach § 8 Abs. 2 BVV

Diese Unterlagenarten bietet **Aus Katalog § 8 BVV** an. Die Bezeichnung ist bereits
DRV-konform und wird so in den Dateinamen übernommen.

| Nr. | Bezeichnung | Unterlage | Unterschriftspflichtig |
| --- | --- | --- | --- |
| 1 | `nachweis_aufenthalt_versicherungsfreiheit_entsendung` | Unterlagen zu Staatsangehörigkeit/Aufenthaltstitel, Versicherungsfreiheit bzw. Befreiung und Entsendung (Abs. 1 Nr. 3, 9, 17) | |
| 2 | `arbeitserlaubnis` | Arbeitserlaubnis bzw. Aufenthaltstitel nach § 15d BeschV | |
| 3 | `meldungen` | Daten der erstatteten Meldungen | |
| 3a | `meldungen_krankenkasse` | Daten der von den Krankenkassen übermittelten Meldungen | |
| 4 | `verzicht_rv_freiheit_minijob` | Verzicht auf die Rentenversicherungsfreiheit (geringfügige Beschäftigung) | |
| 4a | `befreiungsantrag_rv` | Befreiungsantrag nach § 6 Abs. 1b SGB VI mit Eingangsdatum | ja |
| 4b | `aufhebung_befreiung_rv` | Aufhebung der Befreiung nach § 6 Abs. 1b SGB VI | |
| 6 | `niederschrift_nachweisgesetz` | Niederschrift nach dem Nachweisgesetz bzw. Heuervertrag | |
| 7 | `erklaerung_weitere_beschaeftigungen` | Erklärungen zu weiteren kurzfristigen oder geringfügigen Beschäftigungen | |
| 7a | `nachweis_kv_schutz` | Nachweis des Krankenversicherungsschutzes nach § 28a Abs. 9a SGB IV | |
| 8 | `statusfeststellung` | Statusfeststellung nach § 7a SGB IV: Antrag, Bescheid, Gutachten | |
| 9 | `bescheid_28h` | Bescheid der Einzugsstelle nach § 28h Abs. 2 SGB IV | |
| 10 | `entscheidung_finanzamt_studiengebuehren` | Entscheidung des Finanzamts zu Studiengebühren | |
| 11 | `nachweis_elterneigenschaft` | Nachweis der Elterneigenschaft und Kinderzahl nach § 55 Abs. 3 SGB XI | |
| 12 | `auszahlungsverzicht` | Verzicht auf Auszahlung | ja |
| 13 | `aufzeichnungen_aentg_milog` | Aufzeichnungen nach Arbeitnehmer-Entsendegesetz bzw. Mindestlohngesetz | |
| 14 | `bescheinigung_pflegeunterstuetzungsgeld` | Bescheinigung zum Pflegeunterstützungsgeld | |
| 15 | `erklaerung_pflegezeit` | Erklärung zur Pflegezeit | ja |
| 16 | `seefahrt_binnenschifffahrt` | Dokumente der Seefahrt und Binnenschifffahrt | |
| 18 | `bescheinigungen_106_sgb_iv` | Daten der Bescheinigungen nach §§ 106 bis 106c SGB IV | |
| 18a | `ausnahmevereinbarung_art16` | Erklärung zur Ausnahmevereinbarung nach Art. 16 VO (EG) 883/2004 | |
| 19 | `verzicht_versicherungsfreiheit` | Verzicht auf Versicherungsfreiheit (§ 5 Abs. 4 bzw. § 230 Abs. 9 SGB VI) | ja |
| 20 | `zustimmung_127_sgb_iv` | Zustimmung nach § 127 SGB IV | |
| Abs. 1 Nr. 7 | `insolvenzschutz_wertguthaben` | Nachweis über den Insolvenzschutz von Wertguthaben | |

Unterschriftspflichtige Unterlagen brauchen nach Ziffer 2.1.3 der Gemeinsamen Grundsätze
eine qualifizierte elektronische Signatur des Beschäftigten bzw. eine fortgeschrittene
Signatur des Arbeitgebers auf dem Scan. Fehlt sie, muss das Papieroriginal aufbewahrt
werden.

Quelle: [§ 8 BVV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/beitrvv/__8.html)
