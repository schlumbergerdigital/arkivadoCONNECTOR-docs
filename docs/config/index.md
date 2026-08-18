---
title: Einstellungen
description: "Einstellungen des arkivado CONNECTOR konfigurieren: ecoDMS-Verbindung, Exporte, DATEV, Pfade, Oberfläche, Lizenz und Backups."
tags:
    - Einstellungen
    - Konfiguration
    - ecoDMS
    - arkivado CONNECTOR
---

# Einstellungen

Auf der Seite **Einstellungen** konfigurieren Sie den arkivado CONNECTOR vollständig:
Verbindung zu ecoDMS, Exportformate, DATEV, Pfade, Dokumentliste, Oberfläche und Lizenz.

!!! info ""
    Sie erreichen die Seite jederzeit über den Menüpunkt **Einstellungen** in der linken Navigation.

---

## Einrichtung in drei Schritten

Beim ersten Aufruf führt Sie der CONNECTOR durch die Einrichtung. Erst wenn ein Schritt
abgeschlossen ist, wird der nächste angezeigt.

| Schritt | Inhalt | Ergebnis |
| --- | --- | --- |
| 1 – Lizenz aktivieren | Eingabe des Lizenzschlüssels aus Ihrer Bestell-E-Mail | Programm ist freigeschaltet |
| 2 – ecoDMS verbinden | Server-Adresse, Benutzer, Passwort/Token | Verbindung zum Archiv steht |
| 3 – Konfiguration | Alle Einstellungen in Registerkarten | CONNECTOR ist einsatzbereit |

!!! note "Automatischer Verbindungsaufbau"
    Sind bereits Zugangsdaten gespeichert, prüft der CONNECTOR die Verbindung beim Öffnen der
    Seite selbstständig. Dauert dies zu lange oder schlägt es fehl, können Sie über
    **Abbrechen – Zugangsdaten ändern** direkt zum Verbindungsformular wechseln.

---

## Kopfbereich

Oberhalb der Registerkarten stehen zwei Schaltflächen zur Verfügung:

- **ecoDMS-Daten aktualisieren**
  Lädt Klassifizierungsfelder, Dokumentenarten, Status und Ordner neu vom ecoDMS-Server.
  Nutzen Sie die Schaltfläche immer dann, wenn Sie in ecoDMS ein Feld oder eine Dokumentenart
  neu angelegt haben und diese in den Auswahllisten noch nicht erscheint.
- **Doku**
  Öffnet diese Dokumentation in einem neuen Browserfenster.

!!! tip "Speichern nicht vergessen"
    Jeder Bereich besitzt eine eigene Schaltfläche **Speichern**. Änderungen werden erst
    dadurch übernommen. Verlassen Sie die Seite mit ungespeicherten Änderungen, werden Sie
    vorher gewarnt.

---

## Registerkarte „Verbindung"

Hier hinterlegen Sie die Zugangsdaten zu Ihrem ecoDMS-Server.

| Feld | Bedeutung |
| --- | --- |
| Server-Adresse (URL) | Adresse der ecoDMS-API, z. B. `https://ecodms.firma.de:8180` |
| Benutzer | ecoDMS-Benutzer, mit dem der CONNECTOR arbeitet |
| Passwort | Passwort des Benutzers – wird verschlüsselt gespeichert |
| API-Token | Der in der ecoDMS-Administration hinterlegte Connect-Token |
| Bei SSL-Fehler abbrechen | Verhindert die Verbindung zu Servern mit ungültigem Zertifikat |
| Zeitüberschreitung | Wartezeit in Sekunden, bevor eine Anfrage abgebrochen wird |
| Wiederholversuche | Anzahl der automatischen Neuversuche bei Verbindungsproblemen |

!!! warning "Voraussetzung"
    Die API muss in ecoDMS aktiviert sein. Die notwendigen Schritte finden Sie unter
    [Vorbereitung ecoDMS](<../grundeinrichtung/Vorbereitung ecoDMS.md>).

Über **Verbindung testen** prüfen Sie die Eingaben, bevor Sie speichern. Ein bereits
gespeichertes Passwort muss beim erneuten Speichern nicht noch einmal eingegeben werden.

---

## Registerkarte „Export"

Allgemeine Vorgaben, die für alle Exporte gelten, sofern nicht an anderer Stelle überschrieben.

| Einstellung | Bedeutung |
| --- | --- |
| Exportformat | **Excel (.xlsx)** oder **CSV (.csv)** |
| Export-Pfad | Standardordner, in den exportiert wird |
| Datumsfeld | ecoDMS-Datumsfeld, das als Belegdatum ausgewertet wird |
| Exportierte Datei automatisch öffnen | Öffnet die erzeugte Datei nach dem Export |
| Bestehende Datei überschreiben | Aktiv: Datei wird ersetzt. Inaktiv: Dateiname wird hochgezählt (`Liste_1.xlsx`, `Liste_2.xlsx` …) |

---

## Registerkarte „DATEV lokal"

!!! warning "Nicht zu verwechseln mit DATEV Unternehmen Online"
    Diese Registerkarte betrifft ausschließlich den **lokalen** DATEV-Export
    (Rechnungsdaten-Service bzw. DATEV-Belegtransfer-Format).
    Die Anbindung an **DATEV Unternehmen Online** konfigurieren Sie im eigenen Menüpunkt
    **DATEV Online** – siehe [Konfiguration DATEV DUO](<../datev/Konfiguration DATEV DUO.md>).

### DATEV-Konfiguration

| Einstellung | Bedeutung |
| --- | --- |
| Export-Art | **1 – Nur Dateien**: nur die PDF-Belege<br>**2 – Dateien + Liste**: Belege und Übersichtsliste<br>**3 – DATEV XML (Standard)**: Belege mit XML-Steuerdatei |
| Dokumentenart-Feld | ecoDMS-Auswahlfeld, das die Dokumentenart enthält |
| Rechnungseingang-Typ / Rechnungsausgang-Typ | Die Werte, an denen der CONNECTOR Eingangs- bzw. Ausgangsrechnungen erkennt |
| Datumsfeld | Belegdatum |
| Rechnungsnummer-Feld | Textfeld mit der Belegnummer |
| Steuerfeld / Standard-Steuer | Feld mit dem Steuersatz; ist es leer, wird der Standardwert (z. B. `19.00`) verwendet |
| Brutto-Betrag-Feld | Numerisches Feld mit dem Rechnungsbetrag |
| Bemerkung-Feld | Textfeld, das als Bemerkung übergeben wird |
| Zeitfilter verwenden | Schränkt den Export auf den im Dashboard gewählten Zeitraum ein |
| Bestehende Datei überschreiben | Wie in der Registerkarte „Export" |

### Suchfilter

Mit dem Suchfilter legen Sie fest, **welche** Dokumente überhaupt exportiert werden.
Jede Zeile besteht aus Klassifizierungsfeld, Operator und Wert; mehrere Zeilen wirken
zusammen (UND-Verknüpfung).

!!! example "Typischer Filter"
    `Status = Freigegeben` und `StB Export = Haken gesetzt`

### DATEV – Dateinamen

| Einstellung | Bedeutung |
| --- | --- |
| Dateinamen-Schema | Bausteine, getrennt durch Bindestrich, z. B. `<Datum>-<Bemerkung>-<DocID>` |
| Max. Attributlänge im Dateinamen | Kürzt lange Feldinhalte auf die angegebene Zeichenzahl |

!!! tip ""
    Verwenden Sie `<DocID>` im Dateinamen – so bleibt jeder Dateiname eindeutig,
    auch wenn Datum und Bemerkung mehrfach vorkommen.

### DATEV – Lieferanten & Zusatzfelder

Optionale Felder für den erweiterten DATEV-Export: Lieferantenname, Lieferantenstadt,
Zahlungsziel, Info, USt-ID, IBAN und BIC. Felder, die Sie leer lassen, werden nicht
übertragen.

### DATEV – Export-Markierung

Steuert, welche Dokumente noch zu exportieren sind und was nach dem Export in ecoDMS
zurückgeschrieben wird.

| Einstellung | Bedeutung |
| --- | --- |
| Zu-Exportieren-Feld / -Wert | Checkbox-Feld in ecoDMS, das den Export auslöst |
| Bereits-exportiert-Feld / -Wert | Checkbox-Feld, das nach erfolgreichem Export gesetzt wird |
| Export-Datum-Feld | Datumsfeld, in das der Exportzeitpunkt geschrieben wird |

!!! note "Haken gesetzt"
    Die Werte werden als Kontrollkästchen dargestellt: **Haken gesetzt** entspricht in
    ecoDMS dem Wert „angehakt", ein leeres Kästchen dem Wert „nicht angehakt".

---

## Registerkarte „Pfade"

Legt fest, wohin exportiert wird.

1. **Standard Export-Pfad** – Zielordner für alle Dokumente ohne eigene Zuordnung.
2. **Pfade je Dokumentenart** – Wählen Sie unten eine Dokumentenart aus und klicken Sie auf
   **Hinzufügen**. Der CONNECTOR schlägt automatisch einen Unterordner mit dem Namen der
   Dokumentenart vor; den Pfad können Sie anschließend frei anpassen.
3. Über das Papierkorb-Symbol entfernen Sie eine Zuordnung wieder.

!!! tip ""
    In der Auswahlliste erscheinen nur Dokumentenarten, denen noch kein Pfad zugewiesen ist.

---

## Registerkarte „Dokumentliste"

Konfiguration der exportierten Dokumentliste (Excel/CSV).

| Einstellung | Bedeutung |
| --- | --- |
| Exportformat | **Standard** übernimmt die globale Einstellung, alternativ Excel oder CSV |
| Zeitfilter verwenden | Beschränkt die Liste auf den gewählten Zeitraum |
| Suchfilter | Auswahl der zu berücksichtigenden Dokumente |
| Spalten & Kopfzeilen | Per Drag & Drop stellen Sie zusammen, welche ecoDMS-Felder in welcher Reihenfolge als Spalten erscheinen und welche Überschriften verwendet werden |

---

## Registerkarte „Oberfläche"

### Theme

Wählen Sie das Farbschema: **Hell**, **Dunkel**, **Blau** oder **Einhorn**.
Die Auswahl wird sofort als Vorschau angewendet.

### Schaltflächen konfigurieren

Im Vorschauraster gestalten Sie die Schaltflächen des Dashboards:

- **Klicken** öffnet den Editor für Text, Sichtbarkeit, Farbe und Größe.
- **Ziehen** ändert die Reihenfolge.
- **Rechten Rand ziehen** verändert die Breite (1 bis 6 Spalten).
- Ausgeblendete Schaltflächen werden im Raster blass dargestellt.

### Weitere Schaltflächen

Für **Datev Unternehmen Online Export**, **Datei-Export** und **KI-Klassifizierung**
legen Sie jeweils Beschriftung, Farbe und Sichtbarkeit auf dem Dashboard fest.

---

## Registerkarte „Lizenz"

Zeigt den aktuellen Lizenzstatus und erlaubt die Eingabe bzw. den Austausch des
Lizenzschlüssels.

---

## Registerkarte „Erweitert"

### Erweiterte Konfiguration

Hier bearbeiten Sie die vollständige Konfiguration direkt als JSON.

!!! danger "Nur für erfahrene Anwender"
    Fehlerhafte Eingaben können den CONNECTOR unbrauchbar machen. Der Editor prüft beim
    Speichern lediglich, ob gültiges JSON vorliegt. Nutzen Sie diesen Bereich nur nach
    Rücksprache mit dem Support – und legen Sie vorher ein Backup an.

**Neu laden** verwirft Ihre Änderungen im Editor und lädt den gespeicherten Stand.

### Konfigurations-Backups

Der CONNECTOR legt automatisch einmal pro Tag – vor der ersten Änderung – einen Snapshot
der Konfiguration an. Die Aufbewahrungsdauer wird in der Überschrift des Bereichs angezeigt.

- **Backup erstellen** – legt sofort einen zusätzlichen Snapshot an.
- **Aktualisieren** – lädt die Liste der vorhandenen Backups neu.
- **Wiederherstellen** – setzt die Konfiguration auf den gewählten Stand zurück.
  Die aktuelle Konfiguration wird dabei automatisch zuvor gesichert.

---

## Häufige Fragen

??? question "Ein neues ecoDMS-Feld erscheint nicht in den Auswahllisten"
    Klicken Sie oben rechts auf **ecoDMS-Daten aktualisieren**. Der CONNECTOR liest
    Felder, Dokumentenarten, Status und Ordner dann neu vom Server ein.

??? question "Die Verbindung schlägt beim Start fehl"
    Prüfen Sie in der Registerkarte **Verbindung** Adresse, Benutzer und Token. Häufige
    Ursachen sind eine deaktivierte ecoDMS-API, ein falscher Port oder ein ungültiges
    SSL-Zertifikat. Zum Test können Sie **Bei SSL-Fehler abbrechen** vorübergehend
    deaktivieren.

??? question "Meine Änderungen sind nach einem Neustart weg"
    Jeder Bereich muss separat über seine **Speichern**-Schaltfläche gesichert werden.
    Ein Speichern in der Registerkarte „DATEV lokal" übernimmt z. B. keine Änderungen
    aus „Export".

??? question "Wie komme ich zu einem früheren Stand zurück?"
    Über **Erweitert → Konfigurations-Backups → Wiederherstellen**.
