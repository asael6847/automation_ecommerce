from src.abilities.browse_the_web import BrowseTheWeb
from playwright.sync_api import expect



class SearchForProduct:
    def __init__(self,product_name):
        self.product_name = product_name

    def performan_as(self,actor):
        page = actor.ability_to(BrowseTheWeb).page

        # Paso 1: Hacer clic en el menu desplegable
        page.click("#sticky-wrapper > header > div.header-wrapper.container > nav.header-cart > ul > li:nth-child(1) > div")
        # Paso 2: Esperar a que aparezca el input de busqueda
        page.wait_for_selector("input[type='search']")

        # Paso 3: Escribir el nombre del producto y presionar Enter
        page.fill("input[type='search']",self.product_name)

        page.keyboard.press("Enter")

        # Opcional: esperar que la nueva página cargue resultados
        page.wait_for_load_state("networkidle")






