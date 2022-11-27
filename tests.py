from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_set_book_raiting_meaning_five(self):
        book = BooksCollector()
        book.add_new_book('Преступление и наказание')
        book.set_book_rating('Преступление и наказание',5)
        assert book.books_rating == {'Преступление и наказание': 5}

    def test_set_book_raiting_meaning_less_than_one(self):
        book1 = BooksCollector()
        book1.add_new_book('Шерлок Холмс')
        book1.set_book_rating('Шерлок Холмс', 0)
        assert book1.set_book_rating == {'Шерлок Холмс': 1}

    def test_set_book_raiting_meaning_more_than_ten(self):
        book2 = BooksCollector()
        book2.add_new_book('Мастер и Маргарита')
        book2.set_book_rating('Мастер и Маргарита', 11)
        assert book2.set_book_rating == {'Мастер и Маргарита': 1}

    def test_add_new_book_twice(self):
        boo = BooksCollector()
        boo2 = BooksCollector()
        boo.add_new_book('Аленький Цветочек')
        boo2.add_new_book('Аленький Цветочек')
        assert boo2.books_rating == {'Аленький Цветочек' :1}

    def test_get_book_raiting_book_name_raiting(self):
        book3 = BooksCollector()
        book3.add_new_book('Винни Пух')
        assert book3.get_book_rating('Винни Пух') == 1

    def test_get_books_with_specific_rating_rating_list_of_book(self):
        book4 = BooksCollector()
        book5 = BooksCollector()
        book4.add_new_book('Город Грехов')
        book5.add_new_book('Моя Борьба')
        book6 = BooksCollector()
        book6.add_new_book('Емеля')
        book4.set_book_rating('Город Грехов', 2)
        book5.set_book_rating('Моя Борьба',2)
        result = book4.get_books_with_specific_rating(2)
        assert result == ['Город Грехов','Моя Борьба']

    def test_get_books_rating_empty_dictionary_show_empty_dictionary(self):
        dictionary = BooksCollector()
        result = dictionary.get_books_rating()
        assert result == {}

    def test_get_books_rating_not_an_empty_dictionary(self):
        dictionary1 = BooksCollector()
        dictionary1.add_new_book('Тест')
        result = dictionary1.get_books_rating()
        assert result == {'Тест': 1}

    def test_add_book_in_favorites_books_in_rating(self):
        book7 = BooksCollector()
        book7.add_new_book('Маленький принц')
        assert book7.add_book_in_favorites('Маленький принц') == ['Маленький принц']

    def test_add_book_in_favorites_books_not_in_rating(self):
        book8 = BooksCollector()
        assert book8.add_book_in_favorites('Горе от ума') == []

    def test_add_book_in_favorites_books_in_rating_repeat(self):
        book9 = BooksCollector()
        book10 = BooksCollector()
        book10.add_new_book('История')
        assert book9.add_book_in_favorites('История') and book10.add_book_in_favorites('История') == ['История']

    def test_delete_book_from_favorites_book_in_favorites(self):
        book11 = BooksCollector()
        book11.add_new_book('Лаврентий Берия')
        book11.add_book_in_favorites('Лаврентий Берия')
        book11.delete_book_from_favorites('Лаврентий Берия')
        assert book11.favorites == []

    def test_get_list_of_favorites_books_list_not_empty(self):
        book12 = BooksCollector()
        book12.add_new_book('Идиот')
        book12.add_book_in_favorites('Идиот')
        result = book12.get_list_of_favorites_books()
        assert result == ['Идиот']

    def test_add_new_book_book_is_miss_rating_empty(self):
        book13 = BooksCollector()
        book13.add_new_book('Как готовить дома')
        rating = book13.get_books_rating('Такой книги нет в добавленных')
        assert rating is None