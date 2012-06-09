#!/usr/bin/python

"""Command set for the Onkyo TX-NR708.

This file was automatically created by raw_commands_massager.py
from the source file: onkyo_raw_commands.txt
Each command group in the documentation has a seperate list,
and all commands are available in ALL."""


######################
### Power
######################
POWER = [
  ("Power ON", "PWR01"),
  ("Power OFF", "PWR00"),
]
######################
### Audio
######################
AUDIO = [
  ("Mute", "AMT01"),
  ("UnMute", "AMT00"),
  ("MuteToggle", "AMTTG"),
  ("Volume Up", "MVLUP"),
  ("Volume Down", "MVLDOWN"),
]
######################
### Source Select
######################
SOURCE_SELECT = [
  ("VCR/DVR", "SLI00"),
  ("CBL/SAT", "SLI01"),
  ("Game", "SLI02"),
  ("AUX1", "SLI03"),
  ("AUX2", "SLI04"),
  ("DVD", "SLI10"),
  ("TAPE", "SLI20"),
  ("PHONO", "SLI22"),
  ("CD", "SLI23"),
  ("FM", "SLI24"),
  ("AM", "SLI25"),
  ("TUNER", "SLI26"),
  ("Selector Position Wrap-Around Up", "SLIUP"),
  ("Selector Position Wrap-Around Down", "SLIDOWN"),
]
######################
### Speaker AB Control
######################
ZONE = [
  ("Z2ON", "ZPW01"),
  ("Z2OFF", "ZPW00"),
  ("Z2Mute","ZMTTG"),
  ("Z2VOLUP","ZVLUP"),
  ("Z2VOLDOWN","ZVLDOWN"),
  ("z2VCR/DVR", "SLZ00"),
  ("z2CBL/SAT", "SLZ01"),
  ("z2Game", "SLZ02"),
  ("z2AUX1", "SLZ03"),
  ("z2AUX2", "SLZ04"),
  ("z2DVD", "SLZ10"),
  ("z2TAPE", "SLZ20"),
  ("z2PHONO", "SLZ22"),
  ("z2CD", "SLZ23"),
  ("z2FM", "SLZ24"),
  ("z2AM", "SLZ25"),
  ("z2TUNER", "SLZ26"),
]
######################
### Sound modes
######################
SOUND_MODES = [
  ("STEREO", "LMD00"),
  ("DIRECT", "LMD01"),
  ("SURROUND", "LMD02"),
  ("FILM", "LMD03"),
  ("THX", "LMD04"),
  ("ACTION", "LMD05"),
  ("MUSICAL", "LMD06"),
  ("MONO MOVIE", "LMD07"),
  ("ORCHESTRA", "LMD08"),
  ("UNPLUGGED", "LMD09"),
  ("STUDIO-MIX", "LMD0A"),
  ("TV LOGIC", "LMD0B"),
  ("ALL CH STEREO", "LMD0C"),
  ("THEATER-DIMENSIONAL", "LMD0D"),
  ("ENHANCED 7/ENHANCE", "LMD0E"),
  ("MONO", "LMD0F"),
  ("PURE AUDIO", "LMD11"),
  ("MULTIPLEX", "LMD12"),
  ("FULL MONO", "LMD13"),
  ("DOLBY VIRTUAL", "LMD14"),
  ("5.1ch Surround", "LMD40"),
  ("Straight Decode*1", "LMD40"),
  ("Dolby EX/DTS ES", "LMD41"),
  ("Dolby EX*2", "LMD41"),
  ("THX Cinema", "LMD42"),
  ("THX Surround EX", "LMD43"),
  ("U2/S2 Cinema/Cinema2", "LMD50"),
  ("MusicMode", "LMD51"),
  ("Games Mode", "LMD52"),
  ("PLII/PLIIx Movie", "LMD80"),
  ("PLII/PLIIx Music", "LMD81"),
  ("Neo6 Cinema", "LMD82"),
  ("Neo6 Music", "LMD83"),
  ("PLII/PLIIx THX Cinema", "LMD84"),
  ("Neo6 THX Cinema", "LMD85"),
  ("PLII/PLIIx Game", "LMD86"),
  ("Neural Surr*3", "LMD87"),
  ("Neural THX", "LMD88"),
  ("PLII THX Games", "LMD89"),
  ("Neo6 THX Games", "LMD8A"),
  ("Listening Mode Wrap-Around Up", "LMDUP"),
  ("Listening Mode Wrap-Around Down", "LMDDOWN"),
]

ALL = POWER + AUDIO + SOURCE_SELECT + ZONE + SOUND_MODES
