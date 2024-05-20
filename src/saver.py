import json
import os
from src.pars import HHClass


class JSONSaver:
    def dump_to_file(self, vacancies, filename="vacancies.json", directory="data"):
        if not isinstance(vacancies, list):
            raise ValueError("Ожидается, что объект vacancies является списком.")

        full_path = os.path.join(directory, filename)  # Путь к файлу

        try:
            vacancies_data = [vac.to_json() for vac in vacancies]
            with open(full_path, 'w', encoding='UTF-8') as file:
                json.dump(vacancies_data, file, ensure_ascii=False, indent=4)
            print(f"Данные успешно сохранены в {full_path}")
        except AttributeError:
            raise ValueError("Убедитесь, что каждый элемент vacancies имеет метод to_json.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    vac = sorted(HHClass().get_vacancies("python"))
    JSONSaver().dump_to_file(vac)