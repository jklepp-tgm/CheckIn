==============
File List View
==============

Die Dateiliste soll Dateien auflisten sowie Metainformationen und Tags anzeigen
können.

~~~~~~~~~~
Funktionen
~~~~~~~~~~

1. Auflisten der Dateien in einem Ordner

2. Öffnen eines Ordners

~~~~~~~~~~~~
Deliverables
~~~~~~~~~~~~

- Funktionstüchtige Dateiliste.

- Kann, muss aber nicht mit richtigen Dateien arbeiten.
  Dummy Daten sind auch möglich.

===========
Tag Storage
===========

System zum speichern von Tags.

~~~~~~~~~~
Funktionen
~~~~~~~~~~

1. Hinzufügen eines Tags zu einer Datei

2. Lesen der Tags einer Datei

3. Überprüfen ob eine Datei über eine Menge von Tags verfügt

4. Suchen von Dateien mit einer Menge von Tags

~~~~~~~~~~~~
Deliverables
~~~~~~~~~~~~

- Tag Storage System

- Tag Storage API

- Tag Storage API Dokumentation

======================
Metadata- & Tag-Editor
======================

Der Metadata Editor soll sowohl Tags bearbeiten als auch Dateiformatspezifische
Metadaten lesen und ändern können.

Der Metadata Editor soll über die File List View aufgerufen werden können.

Die unterstützung von Dateiformaten soll Modular aufgebaut sein und sich leicht
erweitern lassen.

~~~~~~~~~~
Funktionen
~~~~~~~~~~

1. Hizufügen von Tags zu einer Datei durch einen Benutzer

2. Lesen von Tags einer Datei durch einen Benutzer

3. Ändern der Metadaten einer Datei mit einem unterstützten Dateiformat 
   durch den Benutzer
   
4. Lesen der Metadaten einer Datei mit einem unterstützten Dateiformat nur 
   den Benutzer

5. Hinzufügen von unterstützung für zusätzliche Dateiformate

~~~~~~~~~~~~
Deliverables
~~~~~~~~~~~~

- Metadata- & Tag-Editor UI

- Metadata- & Tag-Editor Logik

- API zur unterstützung weiterer Dateiformate

- API Dokumentation

=============
Plugin System
=============

System zum laden von seperaten Modulen zur Erweiterung der 
Produktfunktionalität

~~~~~~~~~~
Funktionen
~~~~~~~~~~

1. Laden von Modulen aus einem bestimmten Verzeichniss

2. Aktivieren und deaktvieren von Modulen über eine Konfigurationsdatei

~~~~~~~~~~~~
Deliverables
~~~~~~~~~~~~

- Plugin System

- Plugin System Spezifikation

==============
Import Scripts
==============

CheckIn soll über die Möglichkeit verfügen automatisch größere Datenmengen
mit Scripts importieren zu können.

Dafür muss eine API zum hinzufügen von Dateien und ändern von Metadaten und 
Tags zur verfügung gestellt werden.

Cronjobs, zum regelmäßigen Ausführen von Tasks.

~~~~~~~~~~
Funktionen
~~~~~~~~~~

1. Hinzufügen einer Datei über eine API

2. Ändern der Metadaten einer Datei über eine API

3. Ändern der Tags einer Datei über eine API

4. Starten eine Import Scripts durch den Benutzer

5. Automatisches Starten eine Import Scripts durch einen Cronjob

6. Hinzufügen eines Import Scripts durch den Benutzer (möglicherweise über das
   Plugin System)

~~~~~~~~~~~~
Deliverables
~~~~~~~~~~~~

- API zum ändern von Dateien

- Dokumentation

=============
Image Gallery
=============

Übersicht über die Bilder im System oder eines Ordners.

~~~~~~~~~~
Funktionen
~~~~~~~~~~

1. Anzeigen einer Übersicht der Bilder in einer Gallery

2. Anzeigen einzelner Bilder

~~~~~~~~~~~~
Deliverables
~~~~~~~~~~~~

- Image Gallery als Plugin

=============
Search Engine
=============

Suchen von Dateien auf Grund von Dateiname, falls unterstützt Inhalt, falls 
unterstützt Metadaten sowie Tags.

Suchkriterien sollen Modular aufgebaut sein und durch Plugins erweitert werden 
können.

~~~~~~~~~~
Funktionen
~~~~~~~~~~

- Suchen von Dateien

- Erweitern der Suchfunktionalität duch Plugins

~~~~~~~~~~~~
Deliverables
~~~~~~~~~~~~

- Search Engine

- Guide zur benutzung der Search Engine

- API zum eweitern der Search Engine

- Dokumentation zum erweitern der Search Engine
