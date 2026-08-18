---
title: SEPA Export einrichten
description: "SEPA-Export im arkivado CONNECTOR konfigurieren: Rechnungsfelder aus ecoDMS zuordnen, Zahlungsdaten prüfen und Überweisungen vorbereiten."
tags:
    - SEPA
    - SEPA-Export
    - Konfiguration
    - ecoDMS
    - Zahlungsdaten
---
# SEPA Export einrichten

Diese Anleitung führt Sie Schritt für Schritt durch die Einrichtung des
SEPA-Exports. Am Ende können Sie aus Ihren in ecoDMS abgelegten Rechnungen eine
Überweisungsdatei für Ihr Onlinebanking erzeugen.

Nehmen Sie sich für die einmalige Einrichtung etwas Zeit und halten Sie die
IBAN und BIC Ihres Firmenkontos bereit.

!!! info "Voraussetzungen"
    - Das SEPA-Modul ist in Ihrer Lizenz freigeschaltet.
    - Die Verbindung zu ecoDMS ist eingerichtet und getestet
      (siehe [Vorbereitung ecoDMS](<../grundeinrichtung/Vorbereitung ecoDMS.md>)).
    - Ihre Rechnungen werden in ecoDMS klassifiziert z.B. durch [KI](../ki/index.md).

## Schritt 1: Klassifizierungsfelder in ecoDMS anlegen

Der arkivado CONNECTOR liest die Zahlungsdaten aus den Klassifizierungsfeldern
Ihrer Dokumente. Legen Sie diese Felder daher zuerst in ecoDMS an.

Wir empfehlen folgende Felder (die Feldnamen können Sie frei wählen, sie müssen
später nur richtig zugeordnet werden):

| Feld in ecoDMS | Feldtyp in ecoDMS | Wofür wird es verwendet |
|---|---|---|
| Name | Textfeld | Name des Zahlungsempfängers |
| Brutto Betrag | Zahlenfeld | Zu überweisender Rechnungsbetrag |
| IBAN | Textfeld | Konto des Empfängers |
| BIC | Textfeld | Bankleitzahl des Empfängers |
| Verwendungszweck | Textfeld | Zahlungsreferenz, z. B. Rechnungsnummer |
| Zahlungsziel | Datumsfeld | Gewünschtes Ausführungsdatum |
| Datum | Datumsfeld | Belegdatum, für die Zeitraum-Auswahl |
| SEPA Export | Auswahlbox (Haken) | Kennzeichnet Belege, die exportiert werden sollen |
| SEPA Export erfolgt | Auswahlbox (Haken) | Wird nach dem Export gesetzt |
| SEPA Export am | Datumsfeld (optional) | Wird nach dem Export mit dem Datum gefüllt |

!!! note "Nach dem Anlegen neu einlesen"
    Wenn Sie in ecoDMS Felder neu anlegen oder umbenennen, stoppen und starten
    Sie anschließend die ecoDMS API in den ecoDMS-Einstellungen. Danach starten
    Sie den arkivado CONNECTOR neu, damit die Felder zur Auswahl stehen.

## Schritt 2: SEPA-Einstellungen öffnen

1. Öffnen Sie den arkivado CONNECTOR.
2. Wechseln Sie in die **Einstellungen**.
3. Öffnen Sie den Reiter **SEPA**.

Sie sehen drei Bereiche, die Sie nacheinander ausfüllen:

- **SEPA-Konfiguration** – Grundeinstellungen und Feldzuordnung
- **SEPA – Export-Markierung** – welche Belege exportiert werden
- **SEPA – Eigene Bankdaten** – Ihr Konto, von dem gezahlt wird

## Schritt 3: Grundeinstellungen festlegen

Im Bereich **SEPA-Konfiguration** stellen Sie zunächst die allgemeinen Werte ein.

| Einstellung | Empfehlung |
|---|---|
| Schema | `pain.001.003.03` als Standard. Akzeptiert Ihre Bank dieses Format nicht, wählen Sie `pain.001.001.03`. |
| Währung | `EUR` |
| Export-Pfad | Ordner, in dem die fertigen SEPA-Dateien abgelegt werden |

!!! tip "Passendes Schema finden"
    Welches Schema Ihre Bank erwartet, steht meist in der Hilfe Ihres
    Onlinebankings unter „Datei-Upload" oder „Sammlerimport". Wenn der Import
    abgelehnt wird, probieren Sie das jeweils andere Schema.

Beim **Export-Pfad** wählen Sie den Ordner über die Ordnerauswahl aus. Achten
Sie darauf, dass der Ordner dauerhaft erreichbar ist und der arkivado CONNECTOR
dort Dateien schreiben darf. Bei einem Netzlaufwerk verwenden Sie einen Pfad,
der auch für den Dienst erreichbar ist.

## Schritt 4: Felder zuordnen

Jetzt sagen Sie dem Programm, aus welchem ecoDMS-Feld es welche Information
lesen soll. Die Auswahllisten zeigen nur Felder mit passendem Feldtyp an.

| Einstellung im CONNECTOR | Wählen Sie Ihr ecoDMS-Feld für |
|---|---|
| Name-Feld | Name des Zahlungsempfängers |
| Brutto-Betrag-Feld | Rechnungsbetrag |
| IBAN-Feld | IBAN des Empfängers |
| BIC-Feld | BIC des Empfängers |
| Zahlungsziel-Feld | gewünschtes Ausführungsdatum |
| Verwendungszweck-Feld | Verwendungszweck der Zahlung |
| Datumsfeld | Belegdatum für die Zeitraum-Auswahl |

!!! warning "Feld wird nicht angeboten"
    Erscheint ein Feld nicht in der Liste, hat es in ecoDMS meist den falschen
    Feldtyp. Datumsfelder müssen als Datumsfeld, Markierungen als Auswahlbox
    angelegt sein.

## Schritt 5: Optionen wählen

Unter der Feldzuordnung finden Sie vier Schalter:

| Option | Bedeutung | Empfehlung |
|---|---|---|
| Ausführungsdatum auf heute setzen | Alle Zahlungen werden mit dem heutigen Datum erzeugt, unabhängig vom Zahlungsziel | ein |
| Gültiges Ausführungsdatum erzwingen | Verschiebt Termine automatisch auf den nächsten Bankarbeitstag | ein |
| Zeitfilter verwenden | Beschränkt den Export auf einen Zeitraum über das Datumsfeld | aus |
| Bestehende Datei überschreiben | Überschreibt eine vorhandene Exportdatei, statt eine neue Nummer anzuhängen | aus |

!!! note "Automatische Terminkorrektur"
    Ist **Gültiges Ausführungsdatum erzwingen** aktiv, werden Termine an
    Wochenenden und Feiertagen auf den nächsten Bankarbeitstag verschoben.
    Termine in der Vergangenheit werden auf heute gesetzt, Termine sehr weit in
    der Zukunft werden auf die nächsten zwei Wochen begrenzt.

### Suchfilter (optional)

Über den Suchfilter grenzen Sie zusätzlich ein, welche Dokumente überhaupt
berücksichtigt werden, zum Beispiel nur eine bestimmte Dokumentenart oder nur
Belege mit dem Status „Freigegeben". Für den Start können Sie den Filter leer
lassen.

## Schritt 6: Export-Markierung einrichten

Im Bereich **SEPA – Export-Markierung** legen Sie fest, woran der CONNECTOR
erkennt, welche Rechnungen bezahlt werden sollen und welche bereits erledigt
sind.

1. **Zu-Exportieren-Feld**: Wählen Sie Ihr Auswahlbox-Feld, z. B. `SEPA Export`.
2. **Zu-Exportieren-Wert**: Lassen Sie **Haken gesetzt** aktiv. Damit werden alle
   Belege exportiert, bei denen Sie in ecoDMS den Haken setzen.
3. **Bereits-exportiert-Feld**: Wählen Sie z. B. `SEPA Export erfolgt`. Dieses
   Feld setzt der CONNECTOR nach einem erfolgreichen Export.
4. **Bereits-exportiert-Wert**: Ebenfalls **Haken gesetzt** aktiv lassen.
5. **Export-Datum-Feld**: Optional. Wählen Sie ein Datumsfeld, wenn der
   Exportzeitpunkt in ecoDMS vermerkt werden soll, sonst `– Keines –`.

!!! danger "Schutz vor Doppelzahlungen"
    Die Export-Markierung sorgt dafür, dass bereits exportierte Rechnungen bei
    der nächsten Übertragung nicht erneut berücksichtigt werden. Richten Sie
    diesen Bereich unbedingt ein.

## Schritt 7: Eigene Bankdaten hinterlegen

Im Bereich **SEPA – Eigene Bankdaten** tragen Sie das Konto ein, von dem die
Überweisungen ausgeführt werden.

1. Klicken Sie auf **Bank hinzufügen**.
2. Die erste Bank wird automatisch als **Standard** gekennzeichnet.
3. Füllen Sie die drei Felder aus:

    | Feld | Inhalt |
    |---|---|
    | Kontoinh. | Name des Kontoinhabers, wie bei der Bank hinterlegt |
    | IBAN | IBAN Ihres Firmenkontos |
    | BIC | BIC Ihres Firmenkontos |

!!! warning "IBAN und BIC genau prüfen"
    Eine fehlerhafte BIC führt zum Abbruch des Exports. Übernehmen Sie beide
    Angaben am besten direkt aus Ihrem Onlinebanking. Leerzeichen werden
    automatisch entfernt.

### Mehrere Bankkonten verwenden (optional)

Wenn Sie Rechnungen von verschiedenen Konten bezahlen, können Sie mehrere
Banken hinterlegen:

1. Legen Sie in ecoDMS ein **Auswahlfeld** an, das die Bezeichnungen Ihrer
   Konten enthält, zum Beispiel „Hausbank" und „Sparkasse".
2. Wählen Sie dieses Feld im CONNECTOR unter **Bank-Auswahlfeld** aus.
3. Legen Sie über **Bank hinzufügen** je eine Bank pro Auswahlwert an. Die
   Bezeichnung der Bank muss dem Wert im ecoDMS-Auswahlfeld entsprechen.

Beim Export wird dann für jedes Dokument das Konto verwendet, das im
Auswahlfeld steht. Ist das Feld leer oder nicht gesetzt, wird die Standard-Bank
verwendet.

!!! tip "Nur ein Konto?"
    Lassen Sie das **Bank-Auswahlfeld** einfach leer. Dann wird immer die
    Standard-Bank verwendet.

## Schritt 8: Einstellungen speichern

Klicken Sie auf **SEPA speichern**. Ohne das Speichern gehen Ihre Eingaben beim
Verlassen der Seite verloren.

## Schritt 9: Ersten Export testen

Testen Sie die Einrichtung zunächst mit einer einzigen Rechnung:

1. Öffnen Sie ecoDMS und wählen Sie eine geprüfte Rechnung aus.
2. Prüfen Sie, ob Name, IBAN, Betrag, Verwendungszweck und Zahlungsziel
   vollständig eingetragen sind.
3. Setzen Sie den Haken im Feld `SEPA Export`.
4. Wechseln Sie in den arkivado CONNECTOR und starten Sie den SEPA-Export.
5. Öffnen Sie den Export-Ordner. Dort liegt nun eine XML-Datei.
6. Laden Sie die Datei in Ihrem Onlinebanking als **SEPA-Sammelüberweisung**
   hoch und prüfen Sie die Anzeige.

!!! danger "Prüfen vor der Freigabe"
    Der Dateiimport ins Onlinebanking ist noch keine Zahlung. Kontrollieren Sie
    Empfänger, Beträge und Summe in der Übersicht Ihrer Bank und geben Sie die
    Zahlungen erst danach frei.

Nach dem erfolgreichen Export setzt der CONNECTOR in ecoDMS den Haken bei
`SEPA Export erfolgt` und trägt, falls konfiguriert, das Exportdatum ein.

!!! tip "Automatisch als Cronjob ausführen"
	Richten Sie die Aufgabe als Cronjob ein, so wird sie zeitgesteuert vollautomatisch ausgeführt.
	Siehe hier: [Cronjobs definieren](../cronjobs.md).

## Häufige Fragen und Fehler

| Situation | Ursache | Was tun |
|---|---|---|
| Es werden keine Rechnungen exportiert | Haken im Feld `SEPA Export` fehlt oder der Suchfilter passt nicht | Markierung in ecoDMS prüfen, Filter prüfen |
| Meldung zu ungültiger IBAN | Tippfehler in der Klassifizierung des Belegs | IBAN am Beleg in ecoDMS korrigieren |
| Meldung zu ungültiger BIC | BIC des Empfängers oder Ihres Kontos ist fehlerhaft | BIC korrigieren, Schreibweise ohne Leerzeichen |
| Meldung zu fehlerhaftem Betrag | Betragsfeld ist leer, enthält Text oder einen negativen Wert | Betrag am Beleg korrigieren |
| Datei wird nicht erstellt | Export-Pfad existiert nicht oder ist schreibgeschützt | Ordner und Berechtigungen prüfen |
| Bank wird nicht gefunden | Bezeichnung der Bank stimmt nicht mit dem Wert im Auswahlfeld überein | Bezeichnungen angleichen |
| Onlinebanking lehnt die Datei ab | Schema passt nicht zur Bank | Anderes Schema wählen und erneut exportieren |
| Felder fehlen in den Auswahllisten | Felder wurden in ecoDMS neu angelegt | ecoDMS API neu starten, CONNECTOR neu starten |

Einzelne Rechnungen, die wegen fehlerhafter Daten nicht übernommen werden
konnten, finden Sie im Protokoll. Korrigieren Sie den Beleg in ecoDMS und
starten Sie den Export erneut.
