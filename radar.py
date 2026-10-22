        # ----- Vysvětlivky jednotlivých dat -----
        # paket[0:4]   -> f4 f3 f2 f1 - Nový příkaz/Zpráva
        # paket[4:6]   -> 0d 00 - Délka dat
        # paket[6:8]   -> 02 aa - Typ dat
        # paket[8]     -> 00/01/02/03 - 00 = nic / 01 = jen pohyb / 02 = jen dech / 03 = dech i pohyb
        # paket[9:11]  -> 49 00 - Pohybová vzdálenost cíle v centimetrech (poslední zaznamenaný pohyb)
        # paket[11]    -> 00 - Pokud je 0, znamená to že se nikdo nehýbe, 0% pohybu
        # paket[12:14] -> 49 00 - Klidová vzdálenost cíle v centimetrech 
        # paket[14]    -> 59 - Klidová energie 
        # paket[15:17] -> 3a 00 - Celková vzdálenost
        # paket[17:19] -> 55 00 - Kontrolní bajty
        # paket[19:23] -> f8 f7 f6 f5 - Konec 

#knihovna na porty
import serial

import pygame
import sys

#otevře port COM3, 256000 je rychlost dána výrobcem
ser = serial.Serial("COM3", 256000)

HEADER = bytes([0xF4, 0xF3, 0xF2, 0xF1])
buffer = bytearray()

pygame.init()
SIRKA, VYSKA = 600, 400
okno = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Radar")
hodiny = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 32, bold=True)

vzdalenost = 0
bezi = True


while bezi:
    # Zavření okna křížkem
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            bezi = False

    #pokud nic neukazuje, pravděpodobně chyba v zapojení

    # Červený USB do červeného radaru
    # Bílý USB do zeleného radaru
    # Zelený USB do žlutého radaru
    # Černý USB do černého radaru

    #přečte data a vypíše je - pokud nic neukazuje (0), program čeká aby nevytížil procesor
    data = ser.read(ser.in_waiting or 1)
    #port neposílá celé data v jednom kuse (z nejakyho neznamyho duvodu), takže buffer.extend přilepí ty data k sobě
    buffer.extend(data)
    print(data.hex(" "))

    #Hledá začátek zprávy, pokud ji najde vrátí její pozici, pokud ji nenajde vrátí -1
    idx = buffer.find(HEADER)
    # Ověřuje že za headerem máme načtených 23 bajtů (velikost jedné zprávy), pokud není, cyklus čeká na zbytek
    if idx != -1 and len(buffer) >= idx + 23:
        # Vezme tu zprávu, která je za hlavičkou a uloží to do paketu
        paket = buffer[idx:idx + 23]
        # Clean up
        buffer = buffer[idx + 23:]

        # Vytáhne 2 bajty celkové vzdálenosti (index 15 a 16) a přepočítá je na centimetry
        celkova_vzdalenost = paket[15] | (paket[16] << 8)
        print(f"Celková vzdálenost: {celkova_vzdalenost} cm")

    # Vykreslení do Pygame okna
    okno.fill((20, 20, 25))
    text_povrch = font.render(f"Vzdalenost: {celkova_vzdalenost} cm", True, (0, 255, 120))
    okno.blit(text_povrch, (50, 180))
    pygame.display.flip()

ser.close()
pygame.quit()
sys.exit()
