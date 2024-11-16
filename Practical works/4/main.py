import json
from functools import reduce
from typing import List, Dict, Callable, TypeVar
from country import Country

'''
Шаблонный тип.
'''
T = TypeVar('T')

'''
Название файла со странами.
'''
COUNTRIES_FILE_NAME = "countries.json"

'''
Название файла со странами.
'''
COUNTRIES_DATA_FILE_NAME = "countries-data.json"


'''
Возвращает путь к файлу со странами.
'''
def get_file_path(file_name: str) -> str:
    return "./data/" + file_name


'''
Возвращает список стран.
'''
def get_countries(file_name: str) -> T:
    f = open(get_file_path(file_name), encoding="utf-8")
    countries: T = json.load(f)
    f.close()
    return countries


'''
Вывод в консоль результат задач с 1 по 6.
'''
def built_in_functions_test(countries: List[str]) -> None:
    print(f"1. Исходная коллекция стран: {countries}")

    capitalised_countries: List[str] = list(map(lambda country: str(country).upper(), countries))
    print(f"2. Коллекция стран прописными буквами: {capitalised_countries}")

    no_land_countries: List[str] = list(filter(lambda country: not ("land" in str(country).lower()), countries))
    print(f"3. Коллекция стран без land: {no_land_countries}")

    six_symbols_countries: List[str] = list(filter(lambda country: len(str(country)) == 6, countries))
    print(f"4. Коллекция стран с названием из 6 символов: {six_symbols_countries}")

    less_six_symbols_countries: List[str] = list(filter(lambda country: len(str(country)) < 6, countries))
    print(f"5. Коллекция стран с названием менее 6 символов: {less_six_symbols_countries}")

    no_e_countries: List[str] = list(filter(lambda country: not str(country).lower()[0] == 'e', countries))
    print(f"6. Коллекция стран, которые не начинаются с E: {no_e_countries}")


'''
Функция для построения предложения из задания 7.
'''
def construct_countries_sentence(countries: List[str]) -> None:
    allowed_countries: List[str] = [
        'Finland',
        'Sweden',
        'Denmark',
        'Norway',
        'Iceland',
    ]

    allowed_countries_dict: Dict[str, str] = {
        'Finland': 'Финляндия',
        'Sweden': 'Швеция',
        'Denmark': 'Дания',
        'Norway': "Норвегия",
        'Iceland': "Исландия",
    }

    european_countries: List[str] = list(filter(lambda country: country in allowed_countries, countries))

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


'''
Замена map.
'''
def apply_map_to_countries(
        countries: List[str],
        map_func: Callable[[str], str]
) -> List[str]:
    return [map_func(country) for country in countries]


'''
Замена filter.
'''
def apply_filter_to_countries(
        countries: List[str],
        filter_func: Callable[[str], bool]
) -> List[str]:
    return [country for country in countries if filter_func(country)]


'''
Функция для задания 8.
'''
def higher_rank_functions(countries: List[str]) -> None:
    map_func: Callable[[str], str] = lambda country: str(country).upper()
    print(f'8.1 {apply_map_to_countries(countries, map_func)}')

    filter_func: Callable[[str], bool] = lambda country: not ("land" in str(country).lower())
    print(f'8.2 {apply_filter_to_countries(countries, filter_func)}')

    filter_func = lambda country: len(str(country)) == 6
    print(f'8.3 {apply_filter_to_countries(countries, filter_func)}')

    filter_func = lambda country: len(str(country)) < 6
    print(f'8.4 {apply_filter_to_countries(countries, filter_func)}')

    filter_func = lambda country: not str(country).lower()[0] == 'e'
    print(f'8.5 {apply_filter_to_countries(countries, filter_func)}')


'''
Функция для задания 9.
'''
def currying_test(countries: List[str]) -> None:
    def categorize_countries(initial_pattern: str):
        def categorize(countries: List[str]) -> List[str]:
            return [country for country in countries if initial_pattern in country]

        return categorize

    lands: List[str] = categorize_countries('land')(countries)
    print(f"9.1 lands: {lands}")

    ias: List[str] = categorize_countries('ia')(countries)
    print(f"9.2 ias: {ias}")

    islands: List[str] = categorize_countries('island')(countries)
    print(f"9.3 islands: {islands}")

    stans: List[str] = categorize_countries('stan')(countries)
    print(f"9.4 stans: {stans}")


'''
Печатает коллекцию стран в консоль.
'''
def show_countries(countries: List[Country], message = "") -> None:
    len(message) > 0 and print(message)
    for country in countries:
        print(country)


'''
Функция для задания 10.
'''
def process_countries_data() -> None:
    countries_dict: Dict = get_countries(COUNTRIES_DATA_FILE_NAME)
    countries: List[Country] = [Country.dict_to_country(d) for d in countries_dict]
    sorted_countries: List[Country] = sorted(countries, key=lambda country: country.name)
    show_countries(sorted_countries, 'Сортировка по названию')

    sorted_countries = sorted(countries, key=lambda country: country.capital)
    show_countries(sorted_countries, 'Сортировка по столице')

    sorted_countries = sorted(countries, key=lambda country: country.population)
    show_countries(sorted_countries, 'Сортировка по населению')


if __name__ == '__main__':
    countries: List[str] = get_countries(COUNTRIES_FILE_NAME)
    built_in_functions_test(countries)
    construct_countries_sentence(countries)
    higher_rank_functions(countries)
    currying_test(countries)
    process_countries_data()
