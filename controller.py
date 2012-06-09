#!/usr/bin/python
from Tkinter import *
import eiscp

receiver = eiscp.eISCP('10.0.1.41', 60128)
receiver.connectSocket()

def poff():
	receiver.writeCommandFromName('Power OFF')
def pon():
	receiver.writeCommandFromName('Power ON')
def volup():
	receiver.writeCommandFromName('Volume Up')
def voldown():
        receiver.writeCommandFromName('Volume Down')
def volmute():
        receiver.writeCommandFromName('MuteToggle')

def srcDVD():
        receiver.writeCommandFromName('DVD')
def srcVCR():
        receiver.writeCommandFromName('VCR/DVR')
def srcCBL():
        receiver.writeCommandFromName('CBL/SAT')
def srcGame():
        receiver.writeCommandFromName('Game')
def srcAUX1():
        receiver.writeCommandFromName('AUX1')
def srcAUX2():
        receiver.writeCommandFromName('AUX2')
def srcTape():
        receiver.writeCommandFromName('Tape')
def srcFM():
        receiver.writeCommandFromName('FM')
def srcAM():
        receiver.writeCommandFromName('AM')
def srcCD():
        receiver.writeCommandFromName('CD')
def srcPhono():
        receiver.writeCommandFromName('Phono')

def surStereo():
	receiver.writeCommandFromName("STEREO")
def surDirect():
	receiver.writeCommandFromName("DIRECT")
def surAllch():
	receiver.writeCommandFromName("ALL CH STEREO")
def surDigital():
	receiver.writeCommandFromName("5.1ch Surround")
def surPLMov():
	receiver.writeCommandFromName("PLII/PLIIx Movie")
def surPLMus():
	receiver.writeCommandFromName("PLII/PLIIx Music")
def surNeo6Cin():
	receiver.writeCommandFromName("Neo6 Cinema")
def surNeo6Mus():
	receiver.writeCommandFromName("Neo6 Music")
def surPLGame():
	receiver.writeCommandFromName("PLII/PLIIx Game")

def z2On():
	receiver.writeCommandFromName("Z2ON")
def z2Off():
	receiver.writeCommandFromName("Z2OFF")
def z2Mute():
	receiver.writeCommandFromName("Z2Mute")
def z2VolUp():
	receiver.writeCommandFromName("Z2VOLUP")
def z2VolDown():
	receiver.writeCommandFromName("Z2VOLDOWN")

def z2srcDVD():
        receiver.writeCommandFromName('z2DVD')
def z2srcVCR():
        receiver.writeCommandFromName('z2VCR/DVR')
def z2srcCBL():
        receiver.writeCommandFromName('z2CBL/SAT')
def z2srcGame():
        receiver.writeCommandFromName('z2Game')
def z2srcAUX1():
        receiver.writeCommandFromName('z2AUX1')
def z2srcAUX2():
        receiver.writeCommandFromName('z2AUX2')
def z2srcTape():
        receiver.writeCommandFromName('z2Tape')
def z2srcFM():
        receiver.writeCommandFromName('z2FM')
def z2srcAM():
        receiver.writeCommandFromName('z2AM')
def z2srcCD():
        receiver.writeCommandFromName('z2CD')
def z2srcPhono():
        receiver.writeCommandFromName('z2Phono')
root = Tk()

frame = Frame(root)
frame.pack()

def cleanup():
        receiver.disconnectSocket()
	global root
	root.destroy()
mainlabel = Label(frame, text="Primary Commands").grid(row=0, column=1)
quitbut = Button(frame, text="QUIT", fg="red", command=cleanup).grid(row=0, column=2)

ponbut = Button(frame, text="Power ON", command=pon ).grid(row=1, column=0)

poffbut = Button(frame, text="Power OFF", command=poff ).grid(row=1, column=1)
	
volupbut   = Button(frame, text="Volume Up", command=volup,repeatdelay=100, repeatinterval=50).grid(row=2, column=2)
voldownbut = Button(frame, text="Volume Down", command=voldown,repeatdelay=100, repeatinterval=50).grid(row=2, column=0)
volmutebut = Button(frame, text="Mute", command=volmute ).grid(row=2, column=1)

zone2label = Label(frame, text="Zone 2 Commands").grid(row=3,column=1)
zone2onbut = Button(frame, text="Zone 2 ON", command=z2On).grid(row=4,column=1)
zone2offbut = Button(frame, text="Zone 2 OFF", command=z2Off).grid(row=4,column=2)

zone2voldownbut = Button(frame, text="Z2 Volume Down", command=z2VolDown,repeatdelay=100, repeatinterval=50 ).grid(row=5,column=0)
zone2mutebut = Button(frame, text="Z2 Mute", command=z2Mute).grid(row=5,column=1)
zone2volupbut = Button(frame, text="Z2 Volume Up", command=z2VolUp,repeatdelay=100, repeatinterval=50 ).grid(row=5,column=2)

menubar = Menu(root)

sourcemenu = Menu(menubar,tearoff=0)
sourcemenu.add_command(label='DVD', command=srcDVD)
sourcemenu.add_command(label='VCR', command=srcVCR)
sourcemenu.add_command(label='Cable', command=srcCBL)
sourcemenu.add_command(label='Game', command=srcGame)
sourcemenu.add_command(label='AUX1', command=srcAUX1)
sourcemenu.add_command(label='AUX2 (Front)', command=srcAUX2)
sourcemenu.add_command(label='Tape', command=srcTape)
sourcemenu.add_command(label='AM', command=srcAM)
sourcemenu.add_command(label='FM', command=srcFM)
sourcemenu.add_command(label='CD', command=srcCD)
sourcemenu.add_command(label='Phono', command=srcPhono)

surroundmenu = Menu(menubar,tearoff=0)
surroundmenu.add_command(label='Stereo', command=surStereo)
surroundmenu.add_command(label='Direct', command=surDirect)
surroundmenu.add_command(label='All Channel Stereo', command=surAllch)
surroundmenu.add_command(label='Dolby/DTS Direct', command=surDigital)
surroundmenu.add_command(label='PLII/PLIIx Movie', command=surPLMov)
surroundmenu.add_command(label='PLII/PLIIx Music', command=surPLMus)
surroundmenu.add_command(label='PLII/PLIIx Game', command=surPLGame)
surroundmenu.add_command(label='Neo:6 Cinema', command=surNeo6Cin)
surroundmenu.add_command(label='Neo:6 Music', command=surNeo6Mus)


zone2menu = Menu(menubar,tearoff=0)
zone2menu.add_command(label='DVD', command=z2srcDVD)
zone2menu.add_command(label='VCR', command=z2srcVCR)
zone2menu.add_command(label='Cable', command=z2srcCBL)
zone2menu.add_command(label='Game', command=z2srcGame)
zone2menu.add_command(label='AUX1', command=z2srcAUX1)
zone2menu.add_command(label='AUX2 (Front)', command=z2srcAUX2)
zone2menu.add_command(label='Tape', command=z2srcTape)
zone2menu.add_command(label='AM', command=z2srcAM)
zone2menu.add_command(label='FM', command=z2srcFM)
zone2menu.add_command(label='CD', command=z2srcCD)
zone2menu.add_command(label='Phono', command=z2srcPhono)

menubar.add_cascade(label="Sources", menu=sourcemenu)
menubar.add_cascade(label="Surround Mode", menu=surroundmenu)
menubar.add_cascade(label="Zone 2 Sources", menu=zone2menu)

root.config(menu=menubar)
root.title("Onkyo/Integra Systems Controller V1.0")
root.protocol('WM_DELETE_WINDOW', cleanup)
root.mainloop()
