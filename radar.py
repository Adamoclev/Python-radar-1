#knihovna na porty
import serial
#otevře port COM3, 256000 je rychlost dána výrobcem
ser = serial.Serial("COM3", 256000)

while True:
    #přečte data a vypíše je - pokud nic neukazuje (0), program čeká aby nevytížil procesor
    
    #pokud nic neukazuje, pravděpodobně chyba v zapojení

    # Červený USB do červeného radaru
    # Bílý USB do zeleného radaru
    # Zelený USB do žlutého radaru
    # Černý USB do černého radaru
    
    data = ser.read(ser.in_waiting or 1)
    print(data.hex(" "))
