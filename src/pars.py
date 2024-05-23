import requests
from src.vacancies import Vacancy
from abc import ABC, abstractmethod

class Parser(ABC):
    """
    Parser - абстрактный класс, который предоставляет базовую структуру для парсеров вакансий.
    """
    @abstractmethod
    def get_vacancies(self, title):

        pass

class HHClass(Parser):
    """
    HHClass использует API HH.ru для получения списка вакансий, соответствующих заданному запросу.
    """
    @property
    def url(self):
        return self.URL
    
    def _connect_to_api(self):
        pass

    def __init__(self):
        self.__URL = 'https://api.hh.ru/'  # Базовый URL для доступа к API HH.ru

    def get_vacancies(self, title):
        """
        Получает список вакансий с API HH.ru, соответствующих заданному запросу.
        """
        params = {
            'text': title, 
            'area': 1,
            'per_page': 100
            }
        response = requests.get(url=f'{self.__URL}vacancies', params=params)

        # Проверка статуса ответа
        if response.status_code != 200:
            print(f"Ошибка запроса к API: Статус {response.status_code}")
            return 

        # Преобразование ответа в JSON и проверка наличия ключа 'items'
        data = response.json()
        if 'items' not in data:
            print("Ответ API не содержит ключа 'items', проверьте структуру ответа:")
            print(data)
            return 
        #создает список вакансий, извлекая данные из ответа API
        vacancies = []
        for item in response.json()['items']:
            vacancies.append(
                Vacancy(
                    title=item.get('name'),
                    url=item.get('alternate_url'),
                    schedule=item.get('schedule').get('name'),
                    salary=(item.get('salary')
                )
            )
        )
        return vacancies

# Основной блок для тестирования
if __name__ == '__main__':
    hh = HHClass()
    vacancies = hh.get_vacancies('python')
    print(vacancies[0])
