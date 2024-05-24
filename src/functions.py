from src.pars import HH
from src.saver import JSONSaver
from src.vacancies import Vacancy

endl = '\n'

def get_filter_vacancies(vacancies_list: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    '''
    фильтруй вакансии по списку слов
    '''

    #поиск по строковому представления вакасиии в целом, возможно стоит
    #добавить регулярные выражения.
    filtered_vacancies = []
    if filter_words:
        for vacancy in vacancies_list:
            filtered = []
            for word in filter_words:
                if word in vacancies_list:
                    filtered_vacancies.append(vacancy)
        return filtered_vacancies
    else:
        return vacancies_list

def get_vacancies_by_salary(vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    '''
    фильтруй вакансии по зарплате пример '100000-120000'
    '''

    filtered_vacancies = []
    if salary_range:
        between = tuple(int(i) for i in (salary_range.split('-')))
    else:
        return vacancies

    for vacancy in vacancies:
        if between[0] <= vacancy.salary <= between[1]:
            filtered_vacancies.append(vacancy)

    return filtered_vacancies


def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    '''
    верни топ по заданному числу
    '''
    return vacancies[:top_n]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)

def user_interaction():
    """
    Функция взаимодействия с пользователем для поиска вакансий и их сохранения
    """
    fileworker = 'fileworker'
    hh = HH(fileworker)

    search_query = input("Введите поисковый запрос:")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input('Введите диапазон зарплат \033[32mнапример 10000-15000\033[0m: ') # Пример: 100000-150000

    #вызовы функций осуществляющих:
    #фильтрацию по словам
    vacancies_list = hh.get_vacancies(search_query)
   #фильтрацию по словам
    filtered_vacancies = get_filter_vacancies(vacancies_list, filter_words)
    #фильтрацию по зарплате
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #сортировку по зарплате
    sorted_vacancies = sorted(ranged_vacancies, key=lambda x: x.salary, reverse=True)
    #срез по отсортированному списку -> топ
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    #печать
    print_vacancies(top_vacancies)

    #сохраняем данные в файл
    
    file_name = input(f'введи имя файла:{endl}') 
    file_worker = JSONSaver(file_name, top_vacancies)
    file_worker.save()
   
    
    
if __name__ == "__main__":
    user_interaction()