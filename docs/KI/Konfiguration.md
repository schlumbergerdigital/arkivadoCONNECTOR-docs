---
title: Mistral KI konfigurieren
description: "Mistral KI im arkivado CONNECTOR konfigurieren: API-Zugang, Klassifizierungsfelder und automatische ecoDMS-Dokumentenablage einrichten."
tags:
    - Mistral KI
    - Konfiguration
    - ecoDMS
    - API
    - Dokumentenklassifizierung
---

# Mistral KI konfigurieren

Mit der Mistral-KI kann der arkivado CONNECTOR Dokumente automatisch analysieren
und Klassifizierungswerte in ecoDMS setzen. Über Filter legen Sie fest, welche
Dokumente verarbeitet werden und welche Felder nach der Analyse geändert werden.

!!! warning "Voraussetzungen"
	 Für die KI-Klassifizierung benötigen Sie eine gültige Lizenz für das
	 Mistral-Modul, eine funktionierende ecoDMS-Verbindung und einen API-Schlüssel
	 

## KI-Schlüssel und Modell einrichten

Öffnen Sie im Connector im Menü **KI-Klassifizierung** den Bereich
**Basis-Konfiguration**.

### 1. API-Schlüssel hinterlegen

Tragen Sie den API-Schlüssel, den Sie per E-Mail bekommen haben, in das Feld **API-Schlüssel** ein.
Der Schlüssel wird verschlüsselt gespeichert und nach dem Speichern nicht mehr
im Klartext angezeigt.

!!! tip "Schlüssel beim Ändern"
	 Wenn bereits ein Schlüssel gespeichert ist, lassen Sie das Feld leer, um
	 den vorhandenen Schlüssel beizubehalten. Tragen Sie nur dann einen neuen
	 Schlüssel ein, wenn Sie ihn ersetzen möchten.

### 2. Modell auswählen

Wählen Sie im Feld **Modell** das Modell aus, mit dem die Dokumente analysiert
werden sollen. Als Standard ist `mistral-small-latest` voreingestellt.

Mit dem Aktualisieren-Symbol neben der Modellauswahl können Sie die für Ihr
Mistral-Konto verfügbaren Modelle laden. Dafür muss zunächst ein gültiger
API-Schlüssel gespeichert sein.

| Modell | Beschreibung |
|---:|---|
| `mistral-small-latest` | schnelles und günstiges Modell für die meisten Klassifizierungen ausreichend |
| `mistral-medium-latest` | teurer und langsamer, dafür aber genauer als `mistral-small-latest` |

### 3. Kreativität festlegen

Mit dem Regler **Kreativität** bestimmen Sie, wie frei die KI bei ihren
Antworten arbeitet:

| Wert | Bedeutung |
|---:|---|
| `0` | Präzise und reproduzierbar; für Klassifizierungen empfohlen |
| `100` | Maximale Kreativität; für feste Feldwerte in der Regel ungeeignet |

Für eine zuverlässige und wiederholbare Ablage sollte der Wert zunächst auf
`0` bleiben. Erhöhen Sie ihn nur, wenn Sie bewusst flexiblere Interpretationen
benötigen.



## Firmenstammdaten eintragen

Im Bereich **Firmenstammdaten (eigene Firma)** hinterlegen Sie die Daten des
Unternehmens, dessen Dokumente verarbeitet werden. Tragen Sie möglichst
vollständige und eindeutige Angaben ein, zum Beispiel:

```text
Firma: Muster GmbH
Anschrift: Musterstraße 1, 12345 Musterstadt
USt-IdNr.: DE123456789
Steuernummer: 12/345/67890
IBAN: DE00 0000 0000 0000 0000 00
```

Diese Angaben helfen der KI, Eingangs- und Ausgangsdokumente zu unterscheiden.
Bei Feldern wie Firma, Name oder USt-IdNr. kann sie dadurch die Daten des
jeweiligen Geschäftspartners besser erkennen.

## Verarbeitungsbereich festlegen

Der **Allgemeine Filter** bestimmt, welche Dokumente grundsätzlich von der KI
verarbeitet werden.

Verwenden Sie einen Filter, wenn nur bestimmte Dokumente verarbeitet werden
sollen, zum Beispiel Dokumente mit einem bestimmten Status, einer bestimmten
Dokumentenart oder einem Kennzeichenfeld.

!!! danger "Unbedingt Filtern"
    **Ohne Filter** werden **alle Dokumente immer wieder** klassifiziert, es können ***hohe Kosten*** entstehen.

!!! example "Typischer Filter"
	Alle Dokumente im Ordner Eingangskorb, die nicht als Dokumentenart zugeordnet sind und den Status „zu klassifizieren“ haben.

## Dokumentart automatisch bestimmen

Aktivieren Sie den Bereich **Dokumentart-Bestimmung**, wenn die KI zunächst die
Dokumentenart setzen soll. Dieser Schritt wird vor den weiteren
Klassifizierungen ausgeführt.

1. Aktivieren Sie den Schalter **Dokumentart-Bestimmung**.
   
Die KI bestimmt die Dokumentenart, wenn diese auf `nicht zugeordnet` steht.

## Spezial-Klassifizierungen einrichten


!!! tip "Klein anfangen – nur Catch-All verwenden"
	In der Regel benötigen Sie keine Spezial-Klassifizierung. Richten Sie einmal ein
	`Catch-All` ein, also eine Regel, die auf alle Dokumente angewendet wird, und
	legen Sie nur im Notfall eine weitere Regel an. Siehe [hier](#catch-all-verwenden).
    

Mit **Spezial-Klassifizierungen** erstellen Sie eigene Regeln für bestimmte
Dokumenttypen. 

1. Klicken Sie auf **Klassifizierung hinzufügen**.
2. Vergeben Sie einen aussagekräftigen Namen, zum Beispiel
	`Eingangsrechnung` oder `Ausgangsrechnung`.
3. Aktivieren Sie die Klassifizierung über den Schalter.
4. Legen Sie unter **Wann gilt diese Klassifizierung?** die Filterbedingung
	fest.
5. Fügen Sie unter **Zu klassifizierende Felder** die Felder hinzu, die die KI
	aus dem Dokument ermitteln soll.
6. Ergänzen Sie bei Bedarf pro Feld eine zusätzliche Anweisung. Die Hinweise werden in natürlicher Sprache ergänzt.
7. Definieren Sie die Aktionen bei Erfolg und bei Fehler.
  
!!! warning "Keine Schleifen"
	Achten Sie darauf, dass das Dokument nach dem Durchlauf nicht wieder in den Filter fällt.
	Wenn Sie zum Beispiel als Bedingung festlegen, dass der Status `zu klassifizieren` sein muss,
	setzen Sie bei Erfolg den Status auf `prüfen` und im Fehlerfall auf `Fehler`. So werden
	Dokumente nicht mehrfach bearbeitet.


### Zusätzliche Anweisungen

Eine zusätzliche Anweisung bezieht sich immer auf das ausgewählte Feld. Sie
sollte kurz, eindeutig und fachlich konkret sein. Beispiele:

- `Verwende das Rechnungsdatum, nicht das Lieferdatum.`
- `Gib die vollständige IBAN ohne Leerzeichen zurück.`
- `Übernimm die Kundennummer genau wie im Dokument angegeben.`

### Reihenfolge beachten

Wenn mehrere Spezial-Klassifizierungen zutreffen, wird die erste passende
Klassifizierung verwendet. Ordnen Sie daher spezielle Regeln vor allgemeinen
Regeln an. Prüfen Sie besonders, dass eine allgemeine Regel nicht bereits alle
Dokumente abfängt.

## Catch-All verwenden

Der Bereich **Catch-All** wird verwendet, wenn keine Spezial-Klassifizierung
zutrifft.

Aktivieren Sie Catch-All, wenn auch Dokumente ohne passende Spezialregel
verarbeitet werden sollen. Legen Sie anschließend die zu ermittelnden Felder
und die Aktionen wie oben beschrieben fest.

Deaktivieren Sie Catch-All, wenn nicht eindeutig zuordenbare Dokumente
unverändert bleiben sollen.

!!! warning "Keine Schleifen"
     Achten Sie darauf, dass nach dem Durchlauf das Dokument nicht wieder in den Filter fällt. 
     Haben Sie z.B. als defintion: Status muss `zu Klassifizeren` sein. Setzen Sie im Erfolg den Status auf `prüfen` und im Fehlerfall auf `Fehler`. So werden Dokumente nicht mehrfach bearbetet. 

## Aktionen nach der Analyse

### Aktionen bei Erfolg

Unter **Aktionen bei Erfolg** legen Sie fest, welche ecoDMS-Felder nach einer
erfolgreichen Klassifizierung gesetzt werden. Sie können dabei unter anderem
Dokumentenart, Status, Ordner, Hauptordner und eigene ecoDMS-Felder verwenden.

Für jede Aktion wählen Sie ein Feld und anschließend den zu setzenden Wert.
Bei Auswahlfeldern, Statuswerten, Dokumentenarten und Ordnern bietet der
Connector die verfügbaren Werte direkt an.

Optional können Sie ein **Datum-Feld** auswählen. Dort wird der Zeitstempel der
Klassifizierung gespeichert.

### Aktionen bei Fehler

Unter **Aktionen bei Fehler** legen Sie fest, wie ein Dokument bei einer
fehlgeschlagenen Klassifizierung markiert werden soll. Zusätzlich kann ein
Textfeld als **Fehlertext-Feld** ausgewählt werden, in dem die Fehlermeldung
gespeichert wird.

Eine sinnvolle Konfiguration ist beispielsweise:

- Status auf `Fehler` setzen
- ein Kontrollkästchen für die manuelle Nachbearbeitung aktivieren
- ein Textfeld für die Fehlermeldung hinterlegen

## Konfiguration speichern und ausführen
1. Klicken Sie auf **Konfiguration speichern**.
2. Prüfen Sie, ob mindestens ein aktivierter Bereich mindestens ein Feld
	enthält.
3. Klicken Sie auf **Klassifizierung starten**.
4. Beobachten Sie den Fortschritt und die Anzahl erfolgreicher sowie fehlerhafter
	Dokumente.

Nach dem Lauf zeigt der Connector außerdem die verbrauchten Input- und
Output-Tokens an. Fehlerhafte Dokumente werden mit DocID und Fehlermeldung in
der Fehlerliste angezeigt.

!!! warning "Erst mit wenigen Dokumenten testen"
	 Testen Sie eine neue Konfiguration zunächst mit einem kleinen, eindeutig
	 filterbaren Dokumentbestand. Kontrollieren Sie anschließend die gesetzten
	 Werte in ecoDMS, bevor Sie den Filter auf einen größeren Bestand erweitern.


!!! tip "Automatisch als Cronjob ausführen"
	Richten Sie die Aufgabe als Cronjob ein, so wird sie zeitgesteuert vollautomatisch ausgeführt.
	Siehe hier: [Cronjobs definieren](../cronjobs.md).

## Häufige Probleme

| Problem | Mögliche Ursache und Lösung |
|---|---|
| Verbindungstest schlägt fehl | API-Schlüssel prüfen, erneut speichern und Verbindung testen. |
| Keine Modelle verfügbar | API-Schlüssel speichern und anschließend das Aktualisieren-Symbol verwenden. |
| Klassifizierung kann nicht gestartet werden | Lizenz, ecoDMS-Verbindung, Filter und aktivierte Felder prüfen. |
| Keine Aktion wird ausgeführt | Unter **Aktionen bei Erfolg** mindestens ein Feld und einen Wert hinterlegen. |
| Falsche Dokumentart | Firmenstammdaten ergänzen, Kreativität auf `0` setzen und zusätzliche Anweisung präzisieren. |
| Dokumente werden unerwartet erneut verarbeitet | Allgemeinen Filter und die Reihenfolge der Spezial-Klassifizierungen prüfen. |
