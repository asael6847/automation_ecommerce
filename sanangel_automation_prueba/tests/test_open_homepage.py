from src.actors.actor import Actor
from src.abilities.browse_the_web import BrowseTheWeb
from src.tasks.open_home_page import OpenHomePage
from src.tasks.search_for_product import SearchForProduct
from src.tasks.add_to_cart import AddToCart


def test_open_sanangel_homepage():
    #crear actor
    asael = Actor("Asael")
    web_ability = BrowseTheWeb()
    asael.can(web_ability)


    #Abrir pagina
    OpenHomePage("https://sanangel.com.co/").perform_as(asael)


    productos = [("Presente – 12 rosas","2"),
                 ("Versalles","5")]
    
    for nombre,cantidad in productos:
        SearchForProduct(nombre).performan_as(asael)
        AddToCart(cantidad).perform_as(asael)

    web_ability.page.wait_for_timeout(5000)