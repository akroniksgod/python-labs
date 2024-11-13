import json
from functools import reduce

'''
Название файла со странами.
'''
COUNTRIES_FILE_NAME = "countries.json"

'''
Путь к файлу со странами.
'''
COUNTRIES_FILE_PATH = "./data/" + COUNTRIES_FILE_NAME


'''
Возвращает список стран.
'''
def get_countries() -> list[str]:
    f = open(COUNTRIES_FILE_PATH, encoding="utf-8")
    countries: list[str] = json.load(f)
    f.close()
    return countries


'''
Вывод в консоль результат задач с 1 по 6.
'''
def built_in_functions_test(countries: list[str]) -> None:
    print(f"1. Исходная коллекция стран: {countries}")

    capitalised_countries: list[str] = list(map(lambda country: str(country).upper(), countries))
    print(f"2. Коллекция стран прописными буквами: {capitalised_countries}")

    no_land_countries: list[str] = list(filter(lambda country: not ("land" in str(country).lower()), countries))
    print(f"3. Коллекция стран без land: {no_land_countries}")

    six_symbols_countries: list[str] = list(filter(lambda country: len(str(country)) == 6, countries))
    print(f"4. Коллекция стран с названием из 6 символов: {six_symbols_countries}")

    less_six_symbols_countries: list[str] = list(filter(lambda country: len(str(country)) < 6, countries))
    print(f"5. Коллекция стран с названием менее 6 символов: {less_six_symbols_countries}")

    no_e_countries: list[str] = list(filter(lambda country: not str(country).lower()[0] == 'e', countries))
    print(f"6. Коллекция стран, которые не начинаются с E: {no_e_countries}")


'''
Функция для построения предложения из задания 7.
'''
def construct_countries_sentence(countries: list[str]) -> None:
    allowed_countries: list[str] = [
        'Finland',
        'Sweden',
        'Denmark',
        'Norway',
        'Iceland',
    ]

    allowed_countries_dict: dict[str, str] = {
        'Finland': 'Финляндия',
        'Sweden': 'Швеция',
        'Denmark': 'Дания',
        'Norway': "Норвегия",
        'Iceland': "Исландия",
    }

    european_countries: list[str] = list(filter(lambda country: country in allowed_countries, countries))

    def countries_join(countries_str: str, country: str) -> str:
        is_last: bool = european_countries[-1] == country
        is_prev_last: bool = european_countries[-2] == country
        delimiter: str = ', ' if not is_prev_last else ''
        new_country_entry: str = allowed_countries_dict.get(country, '') + delimiter \
            if not is_last \
            else f' и {allowed_countries_dict.get(country, '')} являются странами Северной Европы'
        return countries_str + new_country_entry

    european_countries_str: str = str(reduce(
        countries_join,
        european_countries,
        ''
    ))
    print(f"7. {european_countries_str}")


if __name__ == '__main__':
    countries: list[str] = get_countries()
    built_in_functions_test(countries)
    construct_countries_sentence(countries)
