# CureCrafter_Bioinformatics
- - - -
### v2.0 - 2024
### (C) Simpson College 2017
- - - -

> **Bioinformatics algorithm** 

> Automated design of new molecules based on dataset of docked molecule

- - - -

### GridMol Algorithm ###

* Design molecules and dock with Vina

* Import 3D location of atoms for each docked molecule

* Algorithm creates new molecule based on position of atoms from docked molecules

- - - -

### Dependencies ###

* pyaml

* sqlalchemy
- - - -

### Config ###

NOTE: all directories in root path
NOTE: change Database_Directory for testing 
* Config_Default - valid config defaults
* Config_Testing - valid config for testing

Directories:
* Docked_Directory: 'Folder Name for Importing Raw Vina Dock Files'
* Output_Directory: 'Folder Name for Output Generated Molecule'
* Database_Directory: 'Path for Storing SQL Database of Imported Docked Files'

- - - -

### Testing ###

Fixture databases can be used to test algorithm
NOTE: set config file for testing
* Database_Create: False
* Grid_Size: 1
* Score_Threshold: 0.0
* Origin: X, Y, Z: 0
* Box_Size: X, Y, Z: 10

* straight.sqlite: 10 carbon straight chain
* hexagon.sqlite: 6 carbon hexagon

- - - -

### Folders ###

* Database: SQL database of parsed raw vina dock files
* Docked: raw vina dock files
* GridMol: module for applying algorithm for generating molecule
* Output: algorithm generated molecule - PDB format
* Setup: initializes program features - config file, database, console log

- - - -

