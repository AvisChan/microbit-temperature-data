Temperature = 0
MuseIoT.initialize_wifi()
MuseIoT.set_wifi("", "")
basic.pause(5000)

def on_forever():
    global Temperature
    Temperature = input.temperature()
    MuseIoT.send_thingspeak("96FD1EAET3QAOPU2", Temperature, 0, 0)
    basic.pause(5000)
basic.forever(on_forever)
