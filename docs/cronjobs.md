---
title: Cronjobs
description: Exporte im arkivado CONNECTOR zeitgesteuert ausführen – Cronjobs anlegen, Zeitplan festlegen, Verlauf prüfen und Fehler beheben.
tags:
    - Cronjobs
    - Automatisierung
    - Zeitsteuerung
    - arkivado CONNECTOR
    - Aufgabenplanung
    - Intervall
---

# Cronjobs – Aufgaben automatisch ausführen

Mit **Cronjobs** lassen Sie wiederkehrende Aufgaben automatisch zu festen Zeiten laufen –
zum Beispiel den DATEV-Export jeden Werktag um 18:00 Uhr oder die KI-Klassifizierung alle
30 Minuten. Sie müssen den Export dann nicht mehr manuell auf dem Dashboard starten.

!!! info ""
    Sie erreichen die Seite über den Menüpunkt **Cronjobs** in der linken Navigation.

!!! warning "Wichtigste Voraussetzung"
    Der arkivado CONNECTOR muss zum geplanten Zeitpunkt **laufen**. Ist das Programm
    geschlossen, wird der Zeitpunkt übersprungen und die Aufgabe erst beim nächsten
    planmäßigen Termin ausgeführt. Für den unbeaufsichtigten Dauerbetrieb richten Sie den
    CONNECTOR am besten als Dienst auf einem Server oder einem dauerhaft laufenden
    Rechner ein.

---

## Die Übersicht

Die Tabelle zeigt alle eingerichteten Aufgaben:

| Spalte | Bedeutung |
| --- | --- |
| Name | Frei gewählte Bezeichnung des Jobs |
| Funktion | Die Aufgabe, die ausgeführt wird (z. B. DATEV-Export) |
| Zeitplan | Der Cron-Ausdruck, der den Zeitpunkt festlegt |
| Status | **Aktiviert** – Job läuft planmäßig · **Deaktiviert** – Job pausiert |
| Letzter Lauf | **Erfolgreich**, **Fehler** oder **Läuft** |
| Nächster Lauf | Errechneter nächster Ausführungszeitpunkt |
| Aktionen | Schaltflächen für Ausführen, Pausieren, Verlauf, Bearbeiten, Löschen |

Die Übersicht aktualisiert sich automatisch, solange die Seite geöffnet ist.

---

## Einen Cronjob anlegen

1. Klicken Sie oben rechts auf **Cronjob hinzufügen**.
2. Füllen Sie die Felder aus:

    | Feld | Bedeutung |
    | --- | --- |
    | Funktion | Welche Aufgabe ausgeführt werden soll. Die Liste enthält genau die Exporte, die in Ihrer Konfiguration und Lizenz verfügbar sind. |
    | Name | Eindeutige Bezeichnung, z. B. `DATEV täglich 18 Uhr`. Wird aus der Funktion vorbelegt und kann überschrieben werden. |
    | Zeitplan | Wählen Sie eine **Vorlage** aus der Liste oder tragen Sie einen eigenen Cron-Ausdruck ein. |
    | Beschreibung | Optionaler Hinweis für Ihre Kollegen |
    | Cronjob aktiviert | Legt fest, ob der Job sofort scharfgestellt wird |

3. Mit **Cronjob erstellen** speichern.

!!! tip "Erst testen, dann automatisieren"
    Legen Sie den Job zunächst **deaktiviert** an und starten Sie ihn einmal manuell über
    das Play-Symbol. Prüfen Sie im Verlauf, ob das Ergebnis stimmt, und aktivieren Sie den
    Job erst danach.

### Welche Funktionen stehen zur Auswahl?

Die Auswahlliste wird aus Ihrer Konfiguration erzeugt. Je nach Einrichtung und Lizenz
stehen unter anderem zur Verfügung:

- **DATEV-Export** und **Datev Unternehmen Online Export**
- **SEPA-Export**
- **Dokumentliste / Buchungssätze**
- **Datei-Export** – einzelne Definitionen oder alle Definitionen gemeinsam
- **Metadaten-XML** – einzelne Definitionen oder alle Definitionen gemeinsam
- **KI-Klassifizierung** (Mistral), sofern lizenziert und konfiguriert
- Auswertungen wie **Ordner-**, **Typen-**, **Status-**, **Benutzer-** und
  **Ordner-Rollen-Export**

!!! note ""
    Ein Cronjob nutzt immer die Einstellungen, die Sie unter
    [Einstellungen](config/index.md) für den jeweiligen Export hinterlegt haben – also
    dieselben Suchfilter, Pfade und Formate wie beim manuellen Start.

---

## Der Zeitplan (Cron-Ausdruck)

Ein Cron-Ausdruck besteht aus fünf durch Leerzeichen getrennten Feldern:

```text
┌───────── Minute (0–59)
│ ┌─────── Stunde (0–23)
│ │ ┌───── Tag im Monat (1–31)
│ │ │ ┌─── Monat (1–12)
│ │ │ │ ┌─ Wochentag (0–6, 0 = Sonntag)
│ │ │ │ │
* * * * *
```

Ein `*` bedeutet „jeder Wert". `*/15` bedeutet „alle 15 Einheiten", `1-5` einen Bereich
(Montag bis Freitag) und `7,12,18` eine Aufzählung.

### Fertige Vorlagen

| Vorlage | Ausdruck |
| --- | --- |
| Jeden Tag um 6:00 | `0 6 * * *` |
| Jeden Montag um 8:00 | `0 8 * * 1` |
| Werktags um 18:00 | `0 18 * * 1-5` |
| Jeden 1. des Monats um 9:00 | `0 9 1 * *` |
| Alle 6 Stunden | `0 */6 * * *` |
| Jede Stunde | `0 * * * *` |
| Alle 30 Minuten | `*/30 * * * *` |
| Alle 15 Minuten | `*/15 * * * *` |
| Jede Minute | `* * * * *` |

Unterhalb des Eingabefeldes zeigt der CONNECTOR eine Beschreibung des gewählten Zeitplans
an. Erscheint dort „Benutzerdefinierter Zeitplan", ist der Ausdruck gültig, entspricht aber
keiner der Vorlagen.

!!! example "Eigene Beispiele"
    - `0 7,12,18 * * *` – täglich um 7:00, 12:00 und 18:00 Uhr
    - `5 * * * *` – stündlich, jeweils 5 Minuten nach der vollen Stunde
    - `0 22 * * 0` – sonntags um 22:00 Uhr

!!! warning "Nicht zu häufig ausführen"
    Jeder Lauf erzeugt Last auf dem ecoDMS-Server und verbraucht bei der KI-Klassifizierung
    Kontingente. Wählen Sie den Takt so groß wie möglich und so klein wie nötig.

---

## Aktionen zu einem Cronjob

| Symbol | Aktion | Wirkung |
| --- | --- | --- |
| ▶ | **Jetzt ausführen** | Startet den Job sofort, unabhängig vom Zeitplan. Nur bei aktivierten Jobs möglich. |
| ⏸ / ⏵ | **Pausieren / Fortsetzen** | Setzt den Job aus bzw. nimmt ihn wieder in den Plan auf. Die Konfiguration bleibt erhalten. |
| 🕘 | **Verlauf anzeigen** | Öffnet die Liste der bisherigen Ausführungen. |
| ✏ | **Bearbeiten** | Ändert Name, Zeitplan, Beschreibung und Status. Die Funktion selbst kann nachträglich nicht gewechselt werden. |
| 🗑 | **Löschen** | Entfernt den Job samt Verlauf nach einer Rückfrage. |

!!! note "Berechtigungen"
    Anlegen, Bearbeiten, Löschen und das manuelle Starten sind Administratoren vorbehalten.
    Alle Benutzer können die Übersicht und den Verlauf einsehen.

---

## Verlauf und Fehlerkontrolle

Über **Verlauf anzeigen** sehen Sie zu jedem Job:

- **Gestartet** und **Beendet** – Zeitpunkte der Ausführung
- **Status** – Erfolgreich, Fehler oder Läuft
- **Dauer** – benötigte Laufzeit
- **Nachricht** – Ergebnis bzw. Fehlermeldung

Ein fehlgeschlagener Lauf hält den Zeitplan nicht an: Der Job wird zum nächsten geplanten
Termin erneut ausgeführt. Läuft ein Job noch, wird ein paralleler Start desselben Jobs
übersprungen.

---

## Häufige Fragen

??? question "Warum wurde mein Job nicht ausgeführt?"
    Prüfen Sie in dieser Reihenfolge: Ist der Job **aktiviert**? Lief der CONNECTOR zum
    geplanten Zeitpunkt? Stimmt der Cron-Ausdruck (Spalte **Nächster Lauf** kontrollieren)?
    War der ecoDMS-Server erreichbar? Details finden Sie im Verlauf des Jobs.

??? question "Der Job läuft, exportiert aber keine Dokumente"
    Der Cronjob verwendet die Suchfilter aus den Einstellungen des jeweiligen Exports.
    Findet der Filter keine passenden Dokumente, endet der Lauf erfolgreich – ohne Ergebnis.
    Starten Sie den Export einmal manuell auf dem Dashboard, um den Filter zu prüfen.

??? question "Kann ich denselben Export mehrfach zeitgesteuert ausführen?"
    Ja. Legen Sie einfach mehrere Cronjobs mit derselben Funktion, aber unterschiedlichen
    Namen und Zeitplänen an – zum Beispiel morgens und abends.

??? question "Was passiert, wenn der Rechner nachts aus ist?"
    Die Ausführung entfällt ersatzlos und wird nicht nachgeholt. Planen Sie die Zeiten
    innerhalb der Betriebszeiten oder betreiben Sie den CONNECTOR auf einem Server bzw.
    als Dienst.

??? question "Wie ändere ich die auszuführende Funktion?"
    Die Funktion ist nach dem Anlegen fest. Löschen Sie den Job und legen Sie ihn mit der
    gewünschten Funktion neu an.
