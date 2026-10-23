# Roadmapa a milníky projektu

**Název projektu:** Nízko frekvenční radar s počítačovou aplikací pro vizualizaci pohybu

## Celková roadmapa projektu

* **Zahájení projektu:** 5. 10. 2026
* **Plánovaný termín dokončení:** 29. 1. 2027

## Projektové milníky

- [ ] Milník 1 (do 31. 10. 2026): Zajištění hardwaru
  * Pořízení radarových modulů a nezbytné propojovací kabeláže.
  * *Kritéria splnění:* Hardware je fyzicky dostupný a připravený k prvnímu zapojení.

- [ ] Milník 2 (do 30. 11. 2026): Ověření komunikace a datového toku
  * Testování komunikačních protokolů a schopností detekce v reálném prostředí přes zkušební skript v Pythonu.
  * *Kritéria splnění:* Úspěšné navázání stabilní komunikace s modulem, ověření funkčnosti detekce překážek.

- [ ] Milník 3 (do 31. 12. 2026): Implementace aplikační logiky
  * Vývoj aplikační logiky v Pythonu pro dekódování sériových dat ze senzoru.
  * *Kritéria splnění:* Získaná data ze senzoru jsou spolehlivě překládána do 2D souřadnic a aplikace je schopna identifikovat více cílů současně.

- [ ] Milník 4 (do 29. 1. 2027): Finální vizualizace a UI
  * Naprogramování 2D vizualizace zachycených cílů v prostoru pomocí knihovny pygame.
  * *Kritéria splnění:* Plynulý běh aplikace, vizualizace přesně a v reálném čase odpovídá fyzickému pohybu sledovaných cílů před radarem.
