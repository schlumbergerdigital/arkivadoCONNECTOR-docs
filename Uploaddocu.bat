@REM """~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
@REM  Windows Batch Skript - lädt doku hoch
@REM 			   
@REM 
@REM  Erstellt von:	 Max Schwesig  
@REM  version = "3.0"

@REM  Codierung:    UTF-8	
@REM  Stand:	06.08.2026 Max Schwesig	
 
@REM  Copyright (c) 2026 schlumberger digital. Alle Rechte vorbehalten.
@REM  www.schlumberger.digital
@REM \*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
@echo off
set PYTHONIOENCODING=utf-8
pushd %~dp0
zensical build
python seo_postbuild.py
python upload_docu.py
