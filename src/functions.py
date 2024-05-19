from src.my_parser import HHClass

from src.saver import JSONSaver

def user_interaction():
    """
    Функция взаимодействия с пользователем для поиска вакансий и их сохранения
    """
    hh = HHClass()
    json_saver = JSONSaver()
    
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = list(map(int, input("Введите диапазон зарплат (например, 100000 150000): ").split()))

    vacancies = hh.get_vacancies(search_query)
    #filtered_vacancies = [vac for vac in vacancies if any(word in vac.title for word in filter_words)]
    #ranged_vacancies = [vac for vac in filtered_vacancies if salary_range[0] <= vac.salary <= salary_range[1]]
    sorted_vacancies = sorted(ranged_vacancies, key=lambda x: x.salary, reverse=True)
    top_vacancies = sorted_vacancies[:top_n]

    for vac in top_vacancies:
        print(vac)
    
    json_saver.dump_to_file(top_vacancies)