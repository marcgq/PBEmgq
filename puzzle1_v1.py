"""
Puzzle1_v1
-----------
    Retorna UID en hexadecimal i majúscules d'una targeta Mifare a través
    d'un lector RFID PN532 connectats amb el bus I2C.

    Utilitza la llibreria py532lib (https://pypi.org/project/py532lib/)
    Bloquejant fins que apropem una targeta.
    Podem fer el mètode no bloquejant canviant el paràmetre de
    set_max_entries() per MIFARE_SAFE_RETRIES.

"""
from py532lib.mifare import *

class RfidReader:
   
    # return uid in hexa str
    def read_uid(self):
        card = Mifare()
        card.SAMconfigure()
        card.set_max_retries(MIFARE_WAIT_FOR_ENTRY) 
        received_uid = card.scan_field()
        return received_uid.hex().upper()

       
if __name__ == "__main__":
    rf = RfidReader()
    uid = rf.read_uid()
    print(uid)
