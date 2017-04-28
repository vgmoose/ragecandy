# Rage Candy
A Pokemon Stadium 2 save editor and exporter. **Work in progress!**

Since this program's conception, [a working Stadium 2 dumper](https://projectpokemon.org/forums/forums/topic/40200-gen-2-pokémon-stadium-2-gs-savefile-structure-also-a-dumper-for-registered-teams/) has been posted by @suloku

For dumping save files from a cartridge, [see this wiki](https://github.com/sanni/cartreader/wiki).

## Usage
To use ragecandy, run the program with python. You can either specify a n64 save file as the first argument, 
or enter the path to it when the program prompts for it.
```
python ragecandy.py [.srm file]
```

Currently ragecandy will just try to export and convert the first registered Pokemon in the first registered
team for "Anything goes Lv100". As of this time, it will only give you the raw bytes which can be edited into one of
the gen2 gameboy games with a hex editor.


## Purpose
Pokemon Stadium 2 has a "register pokemon" functionality, where teams from the game boy games can be saved to the N64
cartridge for future use in battles. As Pokemon Stadium 2 uses flash memory to store data, it is more reliable than
the CR2016 battery used in the game boy games. The goal of this tool is to help recover Pokemon who may have previously
been lost due to a failing battery. 

Development for this tool started in 2016, but I've been working with the well-documented generation 2 save format since 2012.
(see [export.py](https://github.com/vgmoose/export.py)). Pokemon Stadium 2's format is a bit different than the game boy games,
but that's the gap that this tool aims to solve!
