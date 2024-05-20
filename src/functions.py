from src.pars import HHClass

hh = HHClass()

def get_filtered_vacancies(vacancies, filter_words):
    """
    фильтрация по ключивым словам 
    """
    filtered_by_keywords = [
        vacancy for vacancy in vacancies
        if any(filter_word in vacancy.title for filter_word in filter_words)
    ]
    
    return filtered_by_keywords

def get_vacancies_by_salary(vacancies, salary_range):
    """
    Фильтрация по диапазону зарплат
    """
    filtered_by_salary = [
        vacancy for vacancy in vacancies
        if vacancy.salary >= salary_range[0]
    ]

    return filtered_by_salary

def get_top_vacancies(sorted_vacancies, top_n):

    return sorted_vacancies[:top_n]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)

def user_interaction():
    """
    Функция взаимодействия с пользователем для поиска вакансий и их сохранения
    """
    
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = list(map(int, input("Введите диапазон зарплат (например, 100000): ").split()))
   
    vacancies_list = hh.get_vacancies(search_query)

    filtered_vacancies = get_filtered_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sorted(ranged_vacancies, key=lambda x: x.salary, reverse=True)
    top_vacancies = sorted_vacancies[:top_n]
    print_vacancies(top_vacancies)
    

if __name__ == "__main__":
    user_interaction()