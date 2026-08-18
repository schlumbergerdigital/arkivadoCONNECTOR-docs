---
title: Datei-Export
description: "Datei-Export im arkivado CONNECTOR konfigurieren: ecoDMS-Dokumente per Filter in lokale Ordner exportieren und nach dem Export zurückschreiben."
tags:
    - Datei-Export
    - Konfiguration
    - ecoDMS
    - Lokaler Export
    - Rückschreibung
---

# Datei-Export

Mit dem **Datei-Export** legen Sie beliebig viele eigene Export-Definitionen an, die
Dokumente aus ecoDMS in lokale Ordner ablegen – z. B. ein Archiv je Kunde.


!!! info "Voraussetzungen"
    - Gültige Lizenz (ohne Lizenz ist die Seite gesperrt)
    - Erreichbarer ecoDMS-Server
    - Benutzerrecht **Datei-Export** – „Ausführen" und/oder „Konfigurieren"

---

## Konfigurieren 


### Definitionen verwalten

- **Neue Definition** legt einen weiteren Export an.
- **Speichern** sichert alle Definitionen. Die Schaltfläche ist nur aktiv, wenn es
  Änderungen gibt.
- Mit dem Griff-Symbol links **ziehen** Sie eine Definition an eine andere Position.
  Die Reihenfolge bestimmt die Abarbeitung beim Gesamtlauf.
- Der Schalter **Aktiv/Pausiert** steuert, ob eine Definition beim Gesamtlauf mitläuft.
  Pausierte Definitionen lassen sich weiterhin einzeln ausführen.
- **Duplizieren** erzeugt eine Kopie – praktisch für ähnliche Exporte.
- **Löschen** entfernt die Definition.
- Über den Pfeil rechts klappen Sie eine Definition auf oder zu.

!!! warning "Erst speichern, dann ausführen"
    Solange eine Definition ungespeicherte Änderungen enthält, ist die Schaltfläche
    **Ausführen** deaktiviert. Der CONNECTOR arbeitet immer mit dem gespeicherten Stand.

---

### Aufbau einer Definition

#### ecoDMS-Felder

Im oberen Kasten sehen Sie alle in ecoDMS verfügbaren Felder
Der Ihnalt der Felder kann für den Export verwendet werden:

- per **Drag & Drop** in „Zielordner" oder „Dateiname" ziehen, **oder**
- einfach **anklicken** – dann wird es an der Cursorposition des zuletzt angeklickten
  Eingabefelds eingefügt. Welches Feld gerade das Ziel ist, steht in der Überschrift
  („Einfügen in: Dateiname").

#### Zielordner (lokal)

Der Ordner, in dem die Dateien gespeichert werden. Er wird bei Bedarf automatisch angelegt.

Auch hier sind Platzhalter erlaubt – **jeder Platzhalter ergibt eine Ordnerebene**:

```text
C:\ecoDMS Daten\Export\<Dokumentenart>\<@date(<Datum>,%Y)>
```

ergibt z. B. `C:\ecoDMS Daten\Export\Rechnungseingang\2026`.

!!! note "Leere Felder"
    Löst ein Platzhalter zu einem leeren Wert auf, entfällt die komplette Ordnerebene –
    es entstehen keine Ordner mit leerem Namen.
    Im Beispiel: `C:\ecoDMS Daten\Export\Rechnungseingang\`

**ecoDMS-Ordnerstruktur übernehmen**
Setzen Sie diesen Haken, wird der Platzhalter `<Ordner>` an den Zielordner angehängt.
Die Dokumente landen dann in der gleichen Ordnerstruktur wie in ecoDMS:

| ecoDMS-Ordner | Zielordner |
| --- | --- |
| `Kunden/Müller` | `C:\Export\Kunden\Müller` |

#### Dateiname-Template

Legt fest, wie die exportierten Dateien heißen. Platzhalter in spitzen Klammern werden
durch die Feldinhalte des Dokuments ersetzt.

```text
<Datum>-<DocID>-<Bemerkung>
```

!!! tip ""
    - Die **Dateiendung wird automatisch ergänzt** – schreiben Sie kein `.pdf` in das Template.
    - Nehmen Sie `<DocID>` mit auf, damit jeder Dateiname eindeutig bleibt.
    - Für Dateinamen unzulässige Zeichen (z. B. `\ / : * ? " < > |`) werden durch `_` ersetzt.
    - Feldinhalte werden auf 50 Zeichen gekürzt.

#### Platzhalter-Funktionen

Neben einfachen Feldern stehen Funktionen zur Verfügung:

=== "Datum formatieren"

    ```text
    <@date(<Belegdatum>,%Y-%m-%d)>
    ```
    
    Formatiert ein Datumsfeld. Ohne Formatangabe wird `%d.%m.%Y` (31.01.2026) verwendet.

    Statt eines Feldes sind auch feste Zeitbezüge möglich:

    | Ausdruck | Bedeutung |
    | --- | --- |
    | `now` | aktuelles Datum/Uhrzeit |
    | `from_time` | Beginn des gewählten Zeitraums |
    | `to_time` | Ende des gewählten Zeitraums |

=== "Ersatzwert"

    ```text
    <@default(<Bemerkung>,ohne Bemerkung)>
    ```

    Ist das Feld leer, wird der zweite Wert eingesetzt. Als Ersatz kann auch ein
    anderes Feld angegeben werden: `<@default(<Bemerkung>,<Dokumentenart>)>`

**Häufige Datumsformate**

| Zeichen | Bedeutung | Beispiel |
| --- | --- | --- |
| `%d` | Tag (2-stellig) | `05` |
| `%m` | Monat (2-stellig) | `03` |
| `%Y` | Jahr (4-stellig) | `2026` |
| `%y` | Jahr (2-stellig) | `26` |
| `%H` / `%M` | Stunde / Minute | `14` / `30` |

!!! example "Ablage nach Jahr und Monat"
    Zielordner: `C:\Export\<@date(<Belegdatum>,%Y)>\<@date(<Belegdatum>,%m)>`
    Dateiname: `<@date(<Belegdatum>,%Y-%m-%d)>-<Bemerkung>-<DocID>`

#### Suchfilter

Legt fest, **welche** Dokumente exportiert werden. Jede Zeile besteht aus Feld, Operator
und Wert; alle Zeilen wirken zusammen. Felder können Sie auch per Drag & Drop aus dem
Feld-Kasten in den Filter ziehen.

!!! danger "Filter ist Pflicht"
    Eine Definition ohne Filter wird nicht ausgeführt – der CONNECTOR meldet
    „Kein Filter konfiguriert". Damit wird verhindert, dass versehentlich das gesamte
    Archiv exportiert wird.

!!! example "Typischer Filter"
    `Status = Freigegeben` · `Datei-Export = aktiviert` · `Datei-Export erledigt = nicht aktiviert`

#### Rückschreibung nach Export

Damit Dokumente nicht bei jedem Lauf erneut exportiert werden, schreibt der CONNECTOR das
Ergebnis nach ecoDMS zurück.

**Bei erfolgreichem Export**

| Einstellung | Bedeutung |
| --- | --- |
| Feld-Aktionen | Beliebig viele Felder, die gesetzt werden – z. B. Haken „Datei-Export erledigt" setzen oder Status auf „Erledigt" ändern |
| Export-Datum-Feld (optional) | Datumsfeld, das auf das aktuelle Datum gesetzt wird |

**Bei fehlerhaftem Export**

| Einstellung | Bedeutung |
| --- | --- |
| Feld-Aktionen | Felder, die im Fehlerfall gesetzt werden – z. B. Status auf „Fehler" |
| Fehlertext-Feld (optional) | Textfeld, in dem die Fehlermeldung gespeichert wird (max. 254 Zeichen) |

!!! tip "Endlosschleifen vermeiden"
    Setzen Sie im Erfolgsfall ein Feld, das im Suchfilter ausgeschlossen ist
    (z. B. Haken „erledigt"). Nur so wird jedes Dokument genau einmal exportiert.

!!! note ""
    Schlägt die Rückschreibung fehl, gilt das Dokument als fehlerhaft und erscheint in der
    Fehlerliste – auch wenn die Datei bereits geschrieben wurde.

---

## Registerkarte „Ausführen"

### Gesamtlauf

**Gesamtlauf starten** arbeitet alle **aktiven** Definitionen in der konfigurierten
Reihenfolge ab. Pausierte Definitionen werden übersprungen.

Während des Laufs sehen Sie:

- einen Fortschrittsbalken mit „x / y Dokumente" und Prozentwert,
- die Anzahl erfolgreicher und fehlerhafter Dokumente,
- eine Kurzübersicht je Definition mit Status (läuft, fertig, übersprungen, Fehler),
- eine ausklappbare **Fehlerliste** mit DocID und Meldung.

Mit **Abbrechen** stoppen Sie den Lauf, mit **Ergebnis schließen** blenden Sie die
Auswertung wieder aus.

Die Schaltfläche ist gesperrt, wenn

- es ungespeicherte Änderungen gibt,
- ecoDMS nicht erreichbar ist oder
- noch keine Definition angelegt wurde.

### Einzelne Definitionen

Darunter können Sie jede Definition einzeln starten – auch pausierte. Das ist ideal zum
Testen einer neuen Konfiguration, bevor Sie sie in den Gesamtlauf aufnehmen.

---

## Empfohlenes Vorgehen

1. In ecoDMS ein Ankreuzfeld für den Export und eines für „erledigt" anlegen
    (siehe [Vorbereitung ecoDMS](<../grundeinrichtung/Vorbereitung ecoDMS.md>)).
2. Neue Definition anlegen und benennen.
3. Zielordner und Dateiname-Template festlegen.
4. Suchfilter setzen – zunächst eng, z. B. auf ein einzelnes Dokument.
5. Rückschreibung konfigurieren.
6. **Speichern**, danach die Definition einzeln **Ausführen** und das Ergebnis im
   Zielordner prüfen.
7. Filter erweitern und die Definition aktiv schalten.

!!! tip "Automatisch als Cronjob ausführen"
	Richten Sie die Aufgabe als Cronjob ein, so wird sie zeitgesteuert vollautomatisch ausgeführt.
	Siehe hier: [Cronjobs definieren](../cronjobs.md).
---

## Häufige Fragen

??? question "Es wird nichts exportiert – die Meldung lautet „Nichts zu exportieren""
    Der Suchfilter trifft auf kein Dokument zu. Prüfen Sie Feldnamen, Operator und Wert –
    und ob die Rückschreibung eines früheren Laufs die Dokumente bereits ausgeschlossen hat.

??? question "„Kein Filter konfiguriert""
    Jede Definition benötigt mindestens eine Filterzeile. Ergänzen Sie den Suchfilter und
    speichern Sie erneut.

??? question "„Zielordner konnte nicht erstellt werden""
    Der angegebene Pfad ist ungültig oder der Benutzer, unter dem der CONNECTOR läuft, hat
    dort keine Schreibrechte. Bei Netzlaufwerken verwenden Sie besser den UNC-Pfad
    (`\\Server\Freigabe\...`) statt eines Laufwerksbuchstabens.

??? question "Ein neues ecoDMS-Feld fehlt in der Auswahl"
    Klicken Sie oben rechts auf **ecoDMS-Daten aktualisieren**.

??? question "Dateien werden bei jedem Lauf erneut exportiert"
    Es fehlt die Rückschreibung oder das zurückgeschriebene Feld ist nicht Teil des
    Suchfilters. Ergänzen Sie im Filter z. B. „erledigt = nicht aktiviert".

??? question "Warum ist „Ausführen" ausgegraut?"
    Entweder gibt es ungespeicherte Änderungen an dieser Definition, oder ecoDMS ist gerade
    nicht erreichbar. Speichern Sie zuerst bzw. prüfen Sie die Verbindung unter
    [Einstellungen](../config/index.md).
