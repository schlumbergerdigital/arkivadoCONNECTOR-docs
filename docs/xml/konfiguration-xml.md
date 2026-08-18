---
title: XML-Export konfigurieren
description: "XML-Export im arkivado CONNECTOR konfigurieren: ecoDMS-Dokumente filtern, XML-Struktur definieren, PDFs anhängen und Daten zurückschreiben."
tags:
    - XML-Export
    - XML
    - Konfiguration
    - ecoDMS
    - Metadaten
    - Rückschreibung
---

# XML-Export

Der **XML-Export** schreibt die Metadaten gefilterter ecoDMS-Dokumente in XML-Dateien –
mit einer Struktur, die Sie selbst festlegen. Auf Wunsch werden die Originaldateien
(PDF, DOCX, TIF …) mit exportiert und im XML referenziert.

Typischer Einsatz: Übergabe von Dokumenten und Metadaten an ein Fremdsystem, das eine
bestimmte XML-Struktur erwartet.

!!! info "Voraussetzungen"
    - **Lizenz für XML** – ohne sie sind Konfiguration und Ausführung gesperrt
    - Erreichbarer ecoDMS-Server
    - Benutzerrecht **XML-Export** – „Ausführen" und/oder „Konfigurieren"

---

## Aufbau der Seite

| Registerkarte | Inhalt |
| --- | --- |
| **Ausführen** | Definitionen starten und Ergebnis sehen |
| **Konfiguration** | Definitionen anlegen und bearbeiten |

Oben rechts:

- **ecoDMS-Daten aktualisieren** – lädt Felder, Dokumentenarten, Status und Ordner neu
  vom ecoDMS-Server.
- **Doku** – öffnet diese Seite.

!!! note "Nur Ausführen-Recht"
    Ohne Konfigurationsrecht sehen Sie die vorhandenen Definitionen mit Namen und der
    Schaltfläche **Ausführen**, aber keine Einstellungen.

---

## Registerkarte „Konfiguration"

### Definitionen verwalten

- **Neue Definition** legt einen weiteren XML-Export an.
- **Speichern** sichert alle Definitionen; nur aktiv, wenn es Änderungen gibt.
- **Duplizieren** erzeugt eine Kopie, sinvoll wenn Sie z.B. pro Dokumentart eine Definition brauchen.
- **Löschen** entfernt die Definition nach Rückfrage.

!!! warning "Erst speichern, dann ausführen"
    Bei ungespeicherten Änderungen ist **Ausführen** deaktiviert.

---

### Ausgabe-Modus

| Modus | Ergebnis |
| --- | --- |
| **Single** | Eine XML-Datei mit allen gefundenen Dokumenten |
| **Multi** | Eine XML-Datei pro Dokument |

Die Auswahl kommt start auf die Gegenseite an. Bei freier Auswahl: `Multi` nehmen. 

### PDF-Dateien mit-exportieren

Ist der Haken gesetzt, lädt der CONNECTOR zusätzlich die Originaldateien aus ecoDMS und
legt sie neben bzw. unterhalb der XML ab. Es erscheinen dann die **PDF-Einstellungen**:

| Einstellung | Bedeutung |
| --- | --- |
| Datei-Name-Template (ohne Endung) | Vorlage für den Dateinamen. Leer = wie der XML-Name. Die Original-Endung (`.pdf`, `.docx`, `.tif` …) wird aus ecoDMS übernommen und automatisch angehängt |
| Datei-Unterordner | Unterordner relativ zum Zielordner. Leer = Dateien liegen neben der XML |
| XML-Element für Datei-Pfad | Name eines zusätzlichen Elements innerhalb des Item-Containers, das den Dateipfad enthält. Leer = kein Pfad im XML |
| Datei-Pfad relativ zum Zielordner | Schreibt den Pfad relativ statt absolut in das XML |

### Zielordner (lokal)

Ordner, in dem XML (und ggf. Dateien) abgelegt werden. Pflichtangabe.

### XML-Dateiname-Template

Vorlage für den Namen der XML-Datei, z. B. `<DocID>.xml`.

- Im Modus **Multi** wird die Vorlage je Dokument aufgelöst.
- Im Modus **Single** bilden nur die **konstanten** Anteile den Dateinamen –
  Feld-Platzhalter werden ignoriert (es gibt kein einzelnes Dokument). Ohne verwertbaren
  Namen heißt die Datei `metadaten.xml`.
- Die Endung `.xml` wird bei Bedarf ergänzt.

!!! warning "Eindeutigen Dateiname"
    Achten Sie darauf einedeutige Bezeichnungen zu nehmen, sonst wird durch einen neuen Export die Dateien überschrieben.
    `uid()` sorgt für eindeutige Name 
---

## Platzhalter

Platzhalter stehen in spitzen Klammern und lassen sich in **Element-Texten**,
**Attributwerten** sowie in den **Dateinamen-Vorlagen** verwenden.

### Feld-Platzhalter

Alle ecoDMS-Klassifizierungsfelder sowie folgende Systemfelder:

| Platzhalter | Inhalt |
| --- | --- |
| `<docid>` | Dokument-ID ohne Kassifizierungs-ID also z.B. `123` |
| `<DocID>` | vollständige Dokument-ID mit kassifizierungs ID also z.B. 123#422 |
| `<Datum>` | Dokumentdatum |
| `<Bemerkung>` | Bemerkung |
| `<Dokumentenart>` | Dokumentenart |
| `<Status>` | Status |
| `<Ordner>` / `<Hauptordner>` | Vollständiger Ordnerpfad |
| `<Ordner_name>` / `<Hauptordner_name>` | Nur das letzte Pfadsegment |
| `<Ordner_external_key>` / `<Hauptordner_external_key>` | Externer Schlüssel aus der ecoDMS-Ordnerstruktur |
| `<Ordner_buzzwords>` / `<Hauptordner_buzzwords>` | Schlagwörter des Ordners |

!!! tip "Per Drag & Drop einfügen"
    Über dem Struktur-Baum finden Sie alle Felder als Chips. Ziehen Sie ein Feld einfach
    in ein Text- oder Attributwert-Feld – der Platzhalter wird komplett eingefügt.

### Funktions-Platzhalter

| Platzhalter | Ergebnis |
| --- | --- |
| `<uid()>` | Neue eindeutige ID (UUID). Jedes Vorkommen erzeugt eine eigene ID |
| `<datum()>` | Heutiges Datum, Standardformat `yyyy-mm-dd` |
| `<datum(dd.mm.yyyy)>` | Heutiges Datum im angegebenen Format |
| `<@date(format)>` | Datumsausdruck (strftime-Format, z. B. `%d.%m.%Y`) |
| `<@ecodmsserver()>` | Hostname des ecoDMS-Servers |
| `<@user>` | Angemeldeter ecoDMS-Benutzer |

**Formatbausteine für `<datum(...)>`**

| Baustein | Bedeutung | Beispiel |
| --- | --- | --- |
| `yyyy` / `yy` | Jahr 4- bzw. 2-stellig | `2026` / `26` |
| `mm` | Monat | `08` |
| `dd` | Tag | `18` |
| `HH` | Stunde | `14` |
| `MM` | Minute | `30` |
| `ss` | Sekunde | `05` |

!!! example ""
    `<datum(yyyy-mm-dd)>_<uid()>.xml` ergibt z. B.
    `2026-08-18_9f2c1b7e4a2d4b1e8c5f0a3d6b9e7c11.xml`

!!! note "Datumswerte im XML"
    Feldwerte, die wie ein Datum aussehen, werden automatisch nach ISO 8601
    (`2026-08-18`) normalisiert – unabhängig vom Anzeigeformat in ecoDMS.

---

## Filter (ecoDMS-Suche)

Legt fest, welche Dokumente exportiert werden. Jede Zeile besteht aus Feld, Operator und
Wert; alle Zeilen wirken zusammen.

!!! danger "Mindestens ein Filter ist Pflicht"
    Ohne Filter lässt sich die Definition nicht speichern.

---

## XML-Struktur

Im Struktur-Baum bauen Sie das Ziel-XML zusammen.

Je Knoten stehen zur Verfügung:

| Element | Bedeutung |
| --- | --- |
| Element-Name | Der XML-Tag, z. B. `Beleg` |
| **Item-Container** | Markierung des Knotens, der je Dokument einmal erzeugt wird, also alle Informationen eines Beleges enthält |
| Attribute | Beliebig viele `name="wert"`-Paare; im Wert sind Platzhalter erlaubt |
| Text / Wert | Inhalt des Elements – nur verfügbar, wenn der Knoten keine Kind-Elemente hat |
| **Kind** | Fügt ein untergeordnetes Element hinzu |
| Duplizieren / Löschen | Knoten kopieren bzw. entfernen (nicht beim Wurzelelement) |

!!! warning "Genau ein Item-Container"
    Der als Item-Container markierte Knoten wird pro gefundenem Dokument einmal
    wiederholt; alles außerhalb bleibt einmalig (Rahmen/Kopfdaten). Ohne Markierung
    lässt sich die Definition nicht speichern. Markieren Sie einen anderen Knoten, wird
    die bisherige Markierung automatisch entfernt.

!!! example "Beispielstruktur"

    ```xml
    <Export erstellt="2026-08-18" system="ecodms-server">   <!-- außerhalb des Item-Containers -->
      <Beleg>                                               <!-- Item-Container -->
        <Id>4711</Id>
        <Datum>2026-08-05</Datum>
        <Art>Rechnungseingang</Art>
        <Bemerkung>Musterlieferant GmbH</Bemerkung>
        <Datei>Dateien\4711.pdf</Datei>
      </Beleg>
      <Beleg> … </Beleg>                                    <!-- Hier das Zweite Deokument -->
    </Export>
    ```

    Erzeugt wurde sie über: Wurzelelement `Export` mit den Attributen
    `erstellt=<datum()>` und `system=<@ecodmsserver()>`, darunter der Item-Container
    `Beleg` mit den Kind-Elementen `Id` = `<DocID>`, `Datum` = `<Datum>`,
    `Art` = `<Dokumentenart>` und `Bemerkung` = `<Bemerkung>`.
    Das Element `Datei` entsteht automatisch, wenn unter „XML-Element für Datei-Pfad"
    der Name `Datei` eingetragen ist.

---

## Rückschreibung nach Export

Damit Dokumente nicht mehrfach exportiert werden, schreibt der CONNECTOR das Ergebnis
nach ecoDMS zurück.

**Bei erfolgreichem Export**

| Einstellung | Bedeutung |
| --- | --- |
| Feld-Aktionen | Felder, die gesetzt werden – z. B. Haken „XML exportiert" oder Status „Erledigt" |
| Export-Datum-Feld (optional) | Datumsfeld, das auf das aktuelle Datum gesetzt wird |

**Bei fehlerhaftem Export**

| Einstellung | Bedeutung |
| --- | --- |
| Feld-Aktionen | Felder, die im Fehlerfall gesetzt werden |
| Fehlertext-Feld (optional) | Textfeld für die Fehlermeldung (max. 254 Zeichen) |

!!! tip ""
    Nehmen Sie das im Erfolgsfall gesetzte Feld in den Filter mit auf (z. B.
    „XML exportiert = nicht aktiviert"), damit jedes Dokument genau einmal exportiert wird.

---

## Registerkarte „Ausführen"

Jede Definition lässt sich einzeln starten. Während des Laufs erscheint ein
Fortschrittsbalken, danach eine grüne bzw. rote Ergebnismeldung.

Die Schaltfläche ist gesperrt, solange es ungespeicherte Änderungen an dieser Definition
gibt.

---

## Prüfungen beim Speichern

Der CONNECTOR speichert erst, wenn für jede Definition gilt:

- [x] Ein Name ist vergeben
- [x] Ein Zielordner ist angegeben
- [x] Mindestens ein Filter ist konfiguriert
- [x] Das Wurzelelement hat einen Tag-Namen
- [x] Genau ein Knoten ist als Item-Container markiert

---

## Empfohlenes Vorgehen

1. Neue Definition anlegen und benennen.
2. Modus wählen (Single oder Multi) und Zielordner setzen.
3. Filter zunächst eng fassen, z. B. auf ein einzelnes Dokument.
4. XML-Struktur aufbauen und den Item-Container markieren.
5. **Speichern** und **Ausführen** – anschließend die erzeugte XML im Zielordner prüfen.
6. Rückschreibung ergänzen und den Filter erweitern.


!!! tip "Automatisch als Cronjob ausführen"
	Richten Sie die Aufgabe als Cronjob ein, so wird sie zeitgesteuert vollautomatisch ausgeführt.
	Siehe hier: [Cronjobs definieren](../cronjobs.md).

---

## Häufige Fragen

??? question "„XML-Modul nicht lizenziert""
    Der XML-Export ist ein separates Modul. Wenden Sie sich an den Vertrieb, um das Modul
    zu Ihrer Lizenz hinzuzufügen.

??? question "„Bitte genau einen Knoten als Item-Container markieren""
    Setzen Sie den Haken **Item-Container** an dem Element, das je Dokument wiederholt
    werden soll – typischerweise am Element direkt unterhalb des Wurzelelements.

??? question "Ein Element bleibt leer"
    Der Platzhalter passt nicht exakt zum Feldnamen in ecoDMS (Groß-/Kleinschreibung und
    Leerzeichen beachten) oder das Feld ist beim Dokument nicht gefüllt. Ziehen Sie das
    Feld am besten per Drag & Drop aus der Feldliste in das Eingabefeld.

??? question "Ich kann keinen Text eingeben"
    Das Feld **Text / Wert** ist nur verfügbar, solange ein Knoten keine Kind-Elemente
    hat. Ein Element kann entweder Text oder Kinder enthalten.

??? question "Wo landen die Originaldateien?"
    Im Zielordner bzw. im angegebenen **Datei-Unterordner**. Damit der Pfad auch im XML
    steht, tragen Sie unter **XML-Element für Datei-Pfad** einen Elementnamen ein.

??? question "Ein neues ecoDMS-Feld fehlt in der Liste"
    Klicken Sie oben rechts auf **ecoDMS-Daten aktualisieren**.
