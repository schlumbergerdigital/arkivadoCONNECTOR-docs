---
title: Einrichtung der Klassifizierungsfelder in ecoDMS für Datev
description: "ecoDMS-Klassifizierungsfelder für den DATEV-Export einrichten: Dokumentarten, Exportmarkierungen und benötigte Rechnungsfelder konfigurieren."
tags:
    - DATEV
    - ecoDMS
    - Klassifizierung
    - Dokumentarten
    - Rechnungsfelder
---

Der Connector kann Dokumente nach bilibgen Kriterien in ecoDMS suchen und Informationen nach dem Export wieder in ecoDMS hinterlegen. 
Für einen sauberen Export empfehlen wir folgende Konfiguration. 

!!! info "Bitte beachten Sie"
    Diese Konfigruation ist unsere *standard* Empfehlung, Anpassungen an Ihr Unternehmen / Prozess sind natürlich jederzeit möglich und ggf. nötig. 


## Einrichtung der Klassifizierungsfelder

Diese sind notwendig um der Schnittstelle zur DATEV (in Klammer unsere vorgeschlagenen Feldnamen) mitzuteilen:
- was soll exportiert werden ("DUO Export")
- wurde exportiert ("DUO erl.")
- wann wurde exportiert ("DUO erl. am")
- Fehlermeldung, falls was nicht geklappt hat ("Fehlermeldung")
    !!! note "Anmerkung"   
    Wenn Sie Feldnamen ändern bzw. neu erstellen, müssen Sie die ecoDMS API unter Einstellungen in ecoDMS stoppen und starten.
Im arkivado Connector werden die neuen bzw. veränderten Klassifizierungen nach einem Neustart der App die neuen oder geänderten Felder wieder eingelesen.   

![Datev Felder](image-14.png)

**Nun ist Ihre Schnittstelle bereit und Sie können im nächsten Schritt den DATEV Unternehmen Online Zugang einrichten.**   

!!! tip "Automatisch als Cronjob ausführen"
	Richten Sie die Aufgabe als Cronjob ein, so wird sie zeitgesteuert vollautomatisch ausgeführt.
	Siehe hier: [Cronjobs definieren](../cronjobs.md).