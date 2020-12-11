#!/usr/bin/env python
"""
    IP weergave (LAN en/of WAN, eth0 en of wlan0)
    Password generator
    system update en upgrade (linux)
    Software installatie (linux) vb.: Apache, MariaDB, PHP,
    system info weergave
    netwerk en/of poortscanner
    gpio pin weergave en hun status
    Een functie die je zelf bedenkt en in het concept past.
"""

from guizero import App, PushButton
import rekenmachine
import passwordgenerator
import achterstevoren
import raadspelletje
import IP_weergave
import NetworkScan
import GPIO
import system_info
import update
import Software

__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Development"

app = App(title="ControlCenter", layout="auto", bg="lightgrey")                  #to create an app

button4 = PushButton(app, raadspelletje.main, text="Raadspelletje")             #to create the pushbuttons
button5 = PushButton(app, IP_weergave.main, text="IP weergeven")
button1 = PushButton(app, rekenmachine.main, text="Rekenmachine")
button6 = PushButton(app, NetworkScan.main, text="Scan het netwerk")
button10 = PushButton(app, Software.main, text="Installeer software")
button8 = PushButton(app, system_info.main, text="Systeeminformatie")
button2 = PushButton(app, achterstevoren.main, text="Woord/zin omdraaien")
button3 = PushButton(app, passwordgenerator.main, text="Wachtwoord generator")
button9 = PushButton(app, update.main, text="Update en upgrade het systeem")
button7 = PushButton(app, GPIO.main, text="Lees de status van de GPIO Pins uit")

app.display()    #to display the app


if __name__ == '__main__':    #code to execute if called from command-line
    rekenmachine.main()
    achterstevoren.main()
    passwordgenerator.main()
    raadspelletje.main()
    IP_weergave.main()
    NetworkScan.main()
    GPIO.main()
    system_info.main()
    update.main()
    Software.main()