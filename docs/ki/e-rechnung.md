---
title: E-Rechnung einrichten
description: E-Rechnungen mit dem arkivado CONNECTOR und Mistral KI für ecoDMS verarbeiten, Daten erkennen und Dokumente automatisch klassifizieren.
tags:
    - E-Rechnung
    - Mistral KI
    - ecoDMS
    - Dokumentenklassifizierung
    - Automatisierung
---
# E-Rechnung einrichten

Der arkivado CONNECTOR erkennt E-Rechnungen automatisch und liest die Werte
direkt aus der Rechnung aus. Das ist genauer als eine KI-Analyse und
**kostet keine Tokens**, weil das Dokument gar nicht erst an die KI geschickt
wird.

Unterstützt werden:

- **XRechnung** (UBL-XML)
- **ZUGFeRD / Factur-X** (PDF mit eingebetteter XML)
- **ebInterface** (Österreich)

Alle übrigen Dokumente durchlaufen wie gewohnt die
[KI-Klassifizierung](konfiguration.md).

!!! warning "Voraussetzungen"
    Die E-Rechnungs-Verarbeitung gehört zum Modul **KI-Klassifizierung** und
    benötigt dieselbe Lizenz. Außerdem muss die ecoDMS-Verbindung eingerichtet
    sein.

!!! info "Wo wird gestartet?"
    Auf dieser Seite legen Sie nur fest, **wie** E-Rechnungen ausgelesen werden.
    Welcher Dokumentbestand verarbeitet wird und wann der Lauf startet, stellen
    Sie weiterhin unter **KI-Klassifizierung** ein (Allgemeiner Filter und
    **Klassifizierung starten**).

## Schritt 1: Verarbeitung aktivieren

1. Öffnen Sie im Menü den Bereich **E-Rechnung**.
2. Schalten Sie oben rechts den Schalter bei
   **E-Rechnungen automatisch auslesen** ein.

Ist der Schalter aus, werden auch E-Rechnungen ganz normal von der KI
klassifiziert – mit entsprechendem Tokenverbrauch.

## Schritt 2: Rechnungsrichtung festlegen

Damit der CONNECTOR weiß, ob eine Rechnung an Sie gestellt wurde
(Eingangsrechnung) oder von Ihnen stammt (Ausgangsrechnung), hinterlegen Sie
Ihre eigenen E-Mail-Adressen.

1. Klicken Sie auf **Adresse hinzufügen**.
2. Tragen Sie eine Adresse ein, zum Beispiel `rechnung@meinefirma.de`.
3. Für alle Adressen einer Domain genügt ein Eintrag wie `@meinefirma.de`.

So wird ausgewertet:

| Wo steht Ihre Adresse in der Rechnung? | Ergebnis |
|---|---|
| beim Rechnungssteller | Ausgangsrechnung |
| beim Rechnungsempfänger | Eingangsrechnung |

### Vorgabe, wenn keine Adresse passt

Enthält eine Rechnung keine Ihrer Adressen, gilt die eingestellte Vorgabe:

| Auswahl | Wirkung |
|---|---|
| Als Eingangsrechnung behandeln | Empfehlung, wenn Sie überwiegend Eingangsrechnungen verarbeiten |
| Als Ausgangsrechnung behandeln | Wenn überwiegend eigene Rechnungen abgelegt werden |
| Richtung offen lassen | Es werden keine richtungsabhängigen Werte gesetzt |

### Bezeichnungen anpassen

Unter **Bezeichnung Eingang** und **Bezeichnung Ausgang** legen Sie fest,
welcher Text in ecoDMS geschrieben wird. Voreingestellt sind
`Rechnungseingang` und `Rechnungsausgang`.

!!! tip "Auf Ihre ecoDMS-Werte abstimmen"
    Wenn Sie diese Bezeichnungen in ein Auswahlfeld oder in die Dokumentenart
    schreiben lassen, müssen die Texte **exakt** den in ecoDMS hinterlegten
    Werten entsprechen. Sonst kann der Wert nicht gesetzt werden.

## Schritt 3: Felder zuordnen

Im Bereich **Feld-Zuordnung** legen Sie fest, welcher Wert aus der Rechnung in
welches ecoDMS-Feld geschrieben wird.

1. Klicken Sie auf **Zuordnung hinzufügen**.
2. Wählen Sie links das **ecoDMS-Feld**.
3. Wählen Sie rechts den **Wert aus der E-Rechnung**.
4. Wiederholen Sie das für jedes Feld, das gefüllt werden soll.

Die Auswahlliste ist in Gruppen aufgeteilt:

| Gruppe | Enthält zum Beispiel |
|---|---|
| Rechnungsrichtung | Richtung (Bezeichnung), Richtung (eingang/ausgang) |
| Geschäftspartner (richtungsabhängig) | Name, Kennung, Straße, PLZ, Ort, USt-IdNr., E-Mail |
| Dokument | Rechnungsnummer, Rechnungsdatum, Fälligkeitsdatum, Leistungszeitraum, Bestellnummer / Leitweg-ID |
| Lieferant (Rechnungssteller) | Name, Anschrift, USt-IdNr., Registernummer, Telefon |
| Kunde (Rechnungsempfänger) | Name, Anschrift, Kennung, E-Mail |
| Beträge | Nettobetrag, Steuerbetrag, Bruttobetrag, Zahlbetrag, Währung, Steuersätze |
| Zahlung | IBAN, BIC, Kontoinhaber, Zahlungsart, Zahlungsbedingungen |

!!! tip "Am besten „Geschäftspartner" verwenden"
    Die Felder der Gruppe **Geschäftspartner** enthalten automatisch die jeweils
    andere Partei: bei einer Eingangsrechnung den Lieferanten, bei einer
    Ausgangsrechnung den Kunden. So brauchen Sie nur **eine** Zuordnung statt je
    einer für Lieferant und Kunde.

### Empfohlene Grundzuordnung

Für den Einstieg genügen meist diese Zuordnungen:

| ecoDMS-Feld | Wert aus der E-Rechnung |
|---|---|
| Name | Geschäftspartner: Name |
| Nummer | Rechnungsnummer |
| Datum | Rechnungsdatum |
| Zahlungsziel | Fälligkeitsdatum |
| Brutto Betrag | Bruttobetrag |
| USt-ID | Geschäftspartner: USt-IdNr. |
| IBAN | IBAN |
| BIC | BIC |
| Dokumentenart | Richtung (Bezeichnung) |

!!! note "Feld wird nicht angeboten"
    Fehlt ein ecoDMS-Feld in der Auswahl, klicken Sie oben rechts auf
    **ecoDMS-Daten aktualisieren**. Neu in ecoDMS angelegte Felder stehen erst
    danach zur Verfügung. Der Hauptordner kann nicht zugeordnet werden.

## Schritt 4: Aktionen bei Erfolg festlegen

Unter **Aktionen bei Erfolg** bestimmen Sie, welche Felder zusätzlich gesetzt
werden, wenn eine Rechnung erfolgreich ausgelesen wurde – zum Beispiel Status,
Dokumentenart oder ein Kontrollkästchen.

Optional wählen Sie ein **Datum-Feld**, in dem der Zeitpunkt der Verarbeitung
gespeichert wird.

!!! danger "Endlosläufe vermeiden"
    Sorgen Sie dafür, dass ein verarbeitetes Dokument nicht erneut in den Filter
    der KI-Klassifizierung fällt. Steht der Filter zum Beispiel auf Status
    `zu Klassifizieren`, setzen Sie bei Erfolg den Status auf `prüfen`.

## Schritt 5: Aktionen bei Fehler festlegen

Unter **Aktionen bei Fehler** legen Sie fest, wie ein Dokument markiert wird,
wenn beim Auslesen etwas schiefgeht. Bewährt hat sich:

- Status auf `Fehler` setzen
- ein Textfeld als **Fehlertext-Feld** hinterlegen, in dem die Meldung landet

## Schritt 6: Speichern und testen

1. Klicken Sie auf **Konfiguration speichern**.
2. Legen Sie eine bekannte E-Rechnung in ecoDMS ab, die Ihrem Filter entspricht.
3. Starten Sie den Lauf unter **KI-Klassifizierung** über
   **Klassifizierung starten**.
4. Prüfen Sie anschließend die gesetzten Werte am Dokument in ecoDMS.

!!! tip "Woran erkenne ich, dass die E-Rechnung genutzt wurde?"
    In der Auswertung des Laufs erscheint das Dokument mit dem Verarbeitungs\-
    schritt **E-Rechnung** und mit **0 Tokens**. Wurde stattdessen die KI
    verwendet, sehen Sie einen Tokenverbrauch.

## Gut zu wissen

- Enthält eine Rechnung ein zugeordnetes Feld nicht, wird dieses Feld einfach
  übersprungen. Die übrigen Werte werden trotzdem geschrieben.
- Leere Werte werden nicht nach ecoDMS zurückgeschrieben. Vorhandene Angaben
  bleiben dadurch erhalten.
- Lässt sich eine erkannte E-Rechnung nicht auslesen, verarbeitet der CONNECTOR
  das Dokument automatisch über die KI weiter. Ein Hinweis dazu steht im
  Protokoll.
- Die E-Rechnungs-Prüfung läuft immer vor der KI-Analyse.

## Häufige Probleme


??? question "Es werden weiterhin Tokens verbraucht"
    Schalter **E-Rechnungen automatisch auslesen** ist aus, oder es handelt sich nicht um eine E-Rechnung, sondern um ein PDF ohne eingebettete XML. 

??? question " Richtung ist immer falsch" 
    Eigene E-Mail-Adressen ergänzen oder die Vorgabe umstellen.

??? question "Dokumentenart wird nicht gesetzt"
    Bezeichnung Eingang/Ausgang stimmt nicht exakt mit dem Wert in ecoDMS überein.

??? question "Einzelne Felder bleiben leer"
    Die Rechnung enthält diesen Wert nicht – im Protokoll steht ein entsprechender Hinweis.

??? question "ecoDMS-Feld fehlt in der Auswahl" 
    Auf **ecoDMS-Daten aktualisieren** klicken.

??? question " Dokumente werden mehrfach verarbeitet "
    Aktionen bei Erfolg so setzen, dass das Dokument nicht mehr in den Filter fällt.

??? question "Bereich ist rot hinterlegt"
    Lizenz für das Modul KI-Klassifizierung prüfen.
