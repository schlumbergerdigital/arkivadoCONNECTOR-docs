@REM """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
@REM  Windows Batch Skript - Startet schlumberger digital Turm Docu
@REM  Im Entwicklungsmodus  - Nicht für Produktiv gedacht 



@REM  Benötigt:  Configuration in params.json				   
@REM  Zur Verwendung mit: turm 
 
@REM  Erstellt von:	 Max Schwesig  
@REM  version = "2.0"

@REM  Codierung:    UTF-8	
@REM  Stand:	31.01.2024 Max Schwesig	
 
@REM  Copyright (c) 2024 schlumberger digital. Alle Rechte vorbehalten.
@REM  www.schlumberger.digital
@REM \*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
@echo off
set PYTHONIOENCODING=utf-8
pushd %~dp0
zensical build 
