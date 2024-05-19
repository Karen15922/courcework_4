class Vacancy:
    """
    Инициализация вакансии с заданными атрибутами
    """

    title: str #Название вакансии
    url: str #URL страницы вакансии
    salary: int #Зарплата предложенная за работу
    city: str #Город, в котором предлагается вакансия

    def __init__(self, title, url, salary, city):
        self.title = title
        self.url = url
        self.city = city
        self.salary = salary or 0

    def __str__(self):
        """
        Строковое представление объекта
        """
        return f'{self.title} ({self.city}): {self.salary}'

    def __repr__(self):
        """
        Официальное строковое представление объекта
        """
        return f'{self.title} ({self.city}): {self.salary}'

    def __gt__(self, other):
        """"
        Определение поведения для оператора '>'. Сравнивает вакансии по зарплате
        """
        return self.salary > other.salary
    
    def to_json(self):
        """
         Конвертирует объект вакансии в JSON-формат.
        """
        return {
            'title': self.title,
            'url': self.url,
            'salary': self.salary,
            'city': self.city
        }