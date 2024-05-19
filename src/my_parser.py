import requests
from abc import ABC, abstractmethod
from src.vacancies import Vacancy


class Parser(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass

class HHClass(Parser):
    """
    Класс для связи с API HH.ru и получения данных о вакансиях
    """
    def __init__(self):
         self.URL = 'https://api.hh.ru/'  #Инициализирует базовый URL для доступа к API

    def get_vacancies(self, title):
        """
        Получает вакансии согласно заданному запросу
        """
        params = {'text': title, 'area': 1, 'per_page': 100}
        response = requests.get(url=f'{self.URL}vacancies', params=params)

        # Проверка статуса ответа
        if response.status_code != 100:
            print(f"Ошибка запроса к API: Статус {response.status_code}")
            return []

        # Преобразование ответа в JSON и проверка наличия ключа 'items'
        data = response.json()
        if 'items' not in data:
            print("Ответ API не содержит ключа 'items', проверьте структуру ответа:")
            print(data)
            return []
        
        vacancies = []
        for item in response.json()['items']:
            vacancies.append(
                Vacancy(
                    title=item.get('name'),
                    url=item.get('alternate_url'),
                    city=item['area']['name'],
                    salary=(item.get('salary') or {}).get('to', 0)
                )
            )
        return vacancies

if __name__ == "__main__":
    hh = HHClass()
    vacancies = hh.get_vacancies('python')
    print(vacancies[0])
