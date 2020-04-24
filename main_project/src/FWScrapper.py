import requests
from bs4 import BeautifulSoup
from Film import Film
from random import randrange


class FWScrapper:
    categories = {
        "Akcja": 28,
        "Animacja": 2,
        "Dokumentalny": 5,
        "Dramat": 6,
        "Familijny": 8,
        "Fantasy": 9,
        "Horror": 12,
        "Komedia": 13,
        "Krótkometrażowy": 50,
        "Kryminał": 15,
        "Melodramat": 16,
        "Niemy": 67,
        "Przygodowy": 20,
        "Romans": 32,
        "Sci-Fi": 33
    }

    listOfFilms = []
    currentCategory = ""

    @staticmethod
    def _downloadListOfFilms(chosen_category, num_page):
        results = []
        try:
            url = "https://www.filmweb.pl/films/search?genres=" + str(
                FWScrapper.categories[chosen_category]) + "&orderBy=popularity&descending=true&page=" + str(num_page)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = results + soup.find_all(class_='hits__item')

            for elem in results:
                title = elem.find(class_='filmPreview__title').text
                year = elem.find(class_='filmPreview__year').text
                rate = elem.find(class_='rateBox__rate').text
                link = "www.filmweb.pl" + elem.find(class_='filmPreview__link')["href"]

                FWScrapper.listOfFilms.append(Film(title, year, link, rate))
            FWScrapper.currentCategory = chosen_category
        except:
            FWScrapper.listOfFilms = []
            FWScrapper.currentCategory = ""

    @staticmethod
    def getRandomFilm(chosen_category, minimal_rate, file):
        if FWScrapper.currentCategory != chosen_category or not FWScrapper.listOfFilms:
            FWScrapper.listOfFilms = []
            FWScrapper._downloadListOfFilms(chosen_category, 1)

        finalListOfFilm = [film for film in FWScrapper.listOfFilms if film.rate >= minimal_rate and film.getTitleWithYear() not in file.getFilmsToSkip()]
        if not finalListOfFilm:
            return None
        else:
            random_choice = randrange(0, len(finalListOfFilm))
            return finalListOfFilm[random_choice]