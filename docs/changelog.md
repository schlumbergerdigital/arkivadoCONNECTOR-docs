---
title: Changelog | arkivado CONNECTOR
description: Aktuelle Änderungen, neue Funktionen und Fehlerbehebungen im arkivado CONNECTOR für ecoDMS, DATEV und automatisierte Exporte.
tags:
    - Changelog
    - arkivado CONNECTOR
    - ecoDMS
    - Updates
---

# Changelog

Alle Aktualisierungen des arkivadoCONNECTORS



## 1.2.1 - <small>28.10.2026</small> { id="1.2.1" }

<b><small>Feature</small></b> 

- Personalakte Export: Elektronische Entgeltunterlagen nach § 8 BVV werden prüfungsfertig für die DRV-Betriebsprüfung exportiert. Die Dateien werden je Mitarbeiter abgelegt und DRV-konform benannt, die Zuordnung erfolgt über die Personalnummer. Jeder Export enthält ein Inhaltsverzeichnis und einen Prüfbericht. Unterlagen mit unzulässigem Format oder ohne Personalnummer werden nicht exportiert, sondern im Prüfbericht aufgeführt. Die Unterlagen-Gruppen können aus dem Katalog nach § 8 Abs. 2 BVV gewählt werden
- Ladebildschirm beim Start zeigt den aktuellen Schritt. Antwortet ecoDMS langsam, kann neu geladen oder ohne Warten fortgefahren werden
- Anmeldung: Bei abgelaufener Sitzung erscheint ein Hinweis, nach der erneuten Anmeldung geht es auf der vorherigen Seite weiter

<b><small>Verbesserung</small></b> 

- KI: Spezial-Klassifizierungen mit Filter auf Felder, die erst die KI ausliest (z. B. USt-ID), greifen wieder. Leere Filterfelder werden vor der Auswahl der Klassifizierung von der KI ermittelt, bereits ausgefüllte Felder bleiben unverändert
- Lizenz: Konnte die Lizenz beim Start nicht geprüft werden (z. B. Netzwerk noch nicht bereit), wird sie regelmäßig erneut geprüft. Ordner-Überwachungen und Seiten werden danach automatisch geladen
- Ordner Upload und XML Import: Die Überwachung startet automatisch neu, wenn der überwachte Ordner gelöscht, umbenannt oder zeitweise nicht erreichbar war
- DATEV DUO: Schlägt die ecoDMS-Suche für eine Dokumentart fehl, wird der Catch-All in diesem Lauf übersprungen, damit keine Dokumente mit falscher Dokumentart an DATEV übertragen werden
- DATEV: Ist die Hauptverbindung abgelaufen, wird beim Abrufen der Mandanten direkt neu verbunden
- ecoDMS: Bleibt nach der Prüfung keine gültige Rolle mit Bearbeitungsrecht übrig, wird das Dokument für alle klassifizierbar gesetzt, statt dass ecoDMS die Klassifizierung ablehnt
- ecoDMS: Verständliche Fehlermeldung, wenn alle Verbindungsversuche fehlschlagen
- Konfiguration übertragen: „Als Datei speichern“ funktioniert jetzt auch im Desktop-Fenster
- Eine bereits laufende Instanz wird auch bei eingerichtetem System-Proxy (z. B. DATEVnet) erkannt
- Windows-Dienst: Läuft der CONNECTOR als Windows-Dienst, öffnet der Start der Desktop-Anwendung nur noch das Fenster zum Dienst und startet keine zweite Instanz. Einstellungen werden so immer in der Konfiguration des Dienstes gespeichert
- Windows-Dienst: Wird der Dienst aus der Oberfläche gestartet, wechselt die Oberfläche automatisch zum Dienst

## 1.2.0 - <small>14.10.2026</small> { id="1.2.0" }

<b><small>Feature</small></b> 

- Ordner Upload: arkivado up ist jetzt im CONNECTOR integriert. Ordner werden überwacht und die Dateien automatisch nach ecoDMS hochgeladen. Die Ordnerstruktur bleibt erhalten. Ändert sich eine Datei, wird eine neue Version des Dokuments in ecoDMS erstellt.
- XML Import: Ordner werden auf XML-Dateien überwacht, das zugehörige Dokument wird nach ecoDMS hochgeladen und mit den Werten aus der XML klassifiziert. Die Zuordnung der XML-Werte zu den ecoDMS-Feldern erfolgt grafisch per Drag & Drop
- Excel-Listen: Es können beliebig viele Dokumentlisten angelegt werden.
- Excel-Listen: Neuer Tabellen-Editor in Excel-Ansicht mit Kopf- und Fußzeilen, Ergebniszeile, Zahlenformaten je Spalte und Link zum Dokument
- Excel-Listen und SEPA: Der Zeitraum kann beim Start abgefragt, dynamisch (z. B. letzter Monat) oder fest hinterlegt werden
- Konfiguration übertragen: Einstellungen (z. B. DATEV, KI, SEPA, Excel-Listen, Suchfilter) lassen sich als JSON exportieren und in einer anderen Installation importieren
- Neustart des CONNECTORS direkt aus der Oberfläche. 
- Ordner Upload: Umstieg von arkivado up. Die Datenbank von arkivado up (filehashes.db) kann übernommen werden, damit bereits hochgeladene Dateien nicht erneut angelegt werden
- Ordner Upload: Regex-Assistent, um Teile aus dem Dateinamen (z. B. Rechnungsnummer oder Datum) per Markierung zu übernehmen
- Ordner Upload und XML Import: Wert-Zuordnung übersetzt ermittelte Werte in ecoDMS-Werte (z. B. GS → Gutschrift), inkl. Export/Import als JSON
- Bewegungsdaten-Backups: Die Journale von Ordner Upload und XML Import werden täglich gesichert. Backups können manuell erstellt und fehlende Journale zurückgespielt werden
- E-Rechnung: Ablageordner je Richtung (Eingang/Ausgang) einstellbar, `<Jahr>` und `<Monat>` werden aus dem Rechnungsdatum gefüllt. Die Bezeichnungen werden aus den Dokumentenarten in ecoDMS ausgewählt
- DATEV: Verständliche Erklärungen zu DATEV-Fehlercodes und HTTP-Fehlern

<b><small>Verbesserung</small></b> 

- Suchfilter: Dynamische Datumswerte und Kalender zur Datumsauswahl
- Upload: Überwachung der Ordner deutlich ressourcenschonender gestaltet. Es werden nur noch geänderte Dateien und betroffene Ordner geprüft
- ecoDMS: Klassifizierungswerte werden vor dem Schreiben geprüft. Werte, die in ecoDMS nicht (mehr) vorhanden sind (z. B. gelöschte Auswahlwerte, Dokumentarten, Status oder Rollen), werden automatisch korrigiert, damit ecoDMS nicht die gesamte Klassifizierung ablehnt. 
- DATEV und KI: Automatisch korrigierte Klassifizierungswerte werden als Warnung im Ergebnis angezeigt
- Ordner Upload und XML Import: Jede Definition hat ein eigenes Journal. Neue Definitionen sind bis zum Speichern inaktiv. Überschneidende Ordner mehrerer Definitionen werden verhindert
- Klassifizierung: Jedes Feld kann nur einmal belegt werden, es sind nur beschreibbare Felder auswählbar. Rollen werden aus ecoDMS ausgewählt
- DATEV: Dateiinhalt und Dateiendung werden vor dem Upload abgeglichen, damit DATEV den Upload nicht ablehnt. Bei Verbindungsfehlern wird der Upload wiederholt
- SEPA: Fehler, die eine ganze SEPA-Datei betreffen, werden allen enthaltenen Belegen zugeordnet
- Benutzerverwaltung: Passwort ändern, alle Berechtigungen auf einmal setzen, Rolle statt Admin-Häkchen
- ecoDMS: Uploads benötigen deutlich weniger Arbeitsspeicher. Leere Dateien (0 KB) werden übersprungen
- DATEV: Multimandanten Upload verbessert. Parallele Läufe und Cronjobs beeinflussen den Mandanten eines laufenden Uploads nicht mehr, gleichzeitige DUO-Exporte werden verhindert
- DATEV: Token-Erneuerung bei parallelen Zugriffen abgesichert
- Ordnerauswahl: Schnellzugriff auf Desktop, Downloads und Dokumente
- Update-Hinweis wird nur noch bei der Windows-Installation angezeigt, nicht im Hosting-Betrieb
- Frontend aktualisiert und diverse Anpassungen an der Oberfläche
- Sicherheit: Berechtigungs- und Pfadprüfungen verschärft
- ecoDMS: Bugfix bei parallelen Uploads konnten gleichnamige Ordner doppelt angelegt werden
- ecoDMS: Fehlertext wurde in einigen Fällen nicht am Dokument gespeichert
- Benutzerverwaltung: Änderungen an Name wurden nicht gespeichert
- Excel/CSV: Leere Felder wurden als „None“ ausgegeben, Zahlenformate wurden gerundet


## 1.1.0 - <small>25.08.2026</small> { id="1.1.0" }

<b><small>Feature</small></b> 

- KI: E-Rechnungen werden automatisch erkannt und klassifiziert, die Dokumente werden nicht mehr mit KI ausgelesen
- Datei Export: Jetzt möglich Dokumente in Ordnerstruktur von ecoDMS zu exportieren
- Datei Export: Attribute für Dokumente können nun auch in Unterordnern exportiert werden
- Dokulinks in der Software eingebaut


<b><small>Verbesserung</small></b> 
- DATEV: Token Refresh verbessert und stabiler
- Banner fix: Banner wird nun korrekt angezeigt, wenn die Lizenz abgelaufen ist


## 1.0.6 - <small>06.08.2026</small> { id="1.0.6" }

<b><small>Feature</small></b> 

- Datei Export: Kann nun Ordner dynamisch anlegen und exportieren 
- Datei Export: Jetzt möglich Dokumente in Ornderstrukrur von ecoDMS zu exportieren
- EcoDMS Time Out für langsame ecoDMS Server einstellbar.
- Logfile Tiefe einstellbar. 


<b><small>Verbesserung</small></b> 
- Frontend: Anhebung auf Nuxt 4 
- Mistral: Bug behoben bei dem durch Kommentare im Ordner die Klassifizierung nicht mehr zuverlässig funktionierte
- Connection Exaution wurde verbessert und ist nun stabiler

  

## 1.0.5 - <small>22.07.2026</small> { id="1.0.5" }

<b><small>Feature</small></b> 

- DATEV DUO Upload kann Dateinamen anpassen 
- Mistral kann nun auch Ordner bestimmen 
- Datei Export Grafisch mit mehreren Ebenen exportieren

<b><small>Verbesserung</small></b> 

- SEPA Bankenfelder verbessert:  Auswahlfeld für verschiedene Banken
- Mistral: KI Kreativität lässt sich anpassen
  


## 1.0.3 - <small>01.07.2026</small> { id="1.0.3" }

  
<b><small>Feature</small></b> 

- Anbindung Mistral.ai zur automatischen Klassifizierung


## 1.0.2 - <small>19.06.2026</small> { id="1.0.2" }

  
<b><small>Feature</small></b> 

- Veröffentlichung der ersten Version  
