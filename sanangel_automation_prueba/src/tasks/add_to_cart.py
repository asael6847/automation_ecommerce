from src.abilities.browse_the_web import BrowseTheWeb

class AddToCart:
    def __init__(self,product_amount):
        self.product_amount = product_amount

    def perform_as(self,actor):
        page = actor.ability_to(BrowseTheWeb).page

        #Paso 1 esperar a estar disponible
        page.wait_for_selector("input[type='number']")

        #Paso 2 ingresar la cantidad del producto
        page.fill("input[type='number']",self.product_amount)

        #Presionar agregar al carrito
        page.click("button[type='submit']")

        