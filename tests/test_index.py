from bs4 import BeautifulSoup

def test_hola_mundo():
    with open("index.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        assert soup.h1.string == "Hola Mundo", "El contenido del H1 no es 'Hola Mundo'"
