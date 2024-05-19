import json

class JSONSaver:
    """
    Класс для сохранения данных о вакансиях в формате JSON
    """
    def dump_to_file(self, vacancies):
        with open('vacancies.json', 'w', encoding='UTF-8') as file:
            json.dump([vac.to_json() for vac in vacancies], file, ensure_ascii=False, indent=4)