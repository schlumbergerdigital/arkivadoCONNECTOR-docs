---
title: XML-Export – Übersicht
description: "XML-Export für ecoDMS mit dem arkivado CONNECTOR: Metadaten in frei definierbarer XML-Struktur ausgeben und Originaldateien mit exportieren."
tags:
    - XML-Export
    - XML
    - ecoDMS
    - Metadaten
    - Export
---

# XML-Export

Der XML-Export übergibt Metadaten aus ecoDMS in einer frei definierbaren XML-Struktur an
Fremdsysteme – auf Wunsch zusammen mit den Originaldateien.

Typischweise um andere Programme mit Daten zu versorgen, wie ERP Systeme, Steuerberater usw. 

Merkmale:

- Struktur des XML per Baum-Editor selbst festlegen (Elemente, Attribute, Texte)
- Frei wählbar: Eine XML mit allen Dokumenten (**Single**) oder eine XML je Dokument (**Multi**)
- Platzhalter für ecoDMS-Felder, Ordnerinformationen, Datum, UUID, Server und Benutzer
- Entweder mit Export der Originaldateien inklusive Pfadangabe im XML oder nur XML
- Rückschreibung nach ecoDMS, damit jedes Dokument nur einmal exportiert wird

!!! info "Lizenz"
    Der XML-Export benötigt die XML-Lizenz.

[XML-Export konfigurieren](konfiguration-xml.md){ .md-button .md-button--primary }
