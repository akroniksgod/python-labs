from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
import pandas as pd
from typing import List, Dict

# Экземпляр для fast api приложения.
app = FastAPI()

# Конфигурация для CORS.
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

# Путь к файлам по данным
DATASETS_PATH: str = '../datasets/'

# Осадки
rainfall_df: pd.DataFrame = pd.read_csv(f'{DATASETS_PATH}final_rainfall.csv')

# Температуры
temperature_df: pd.DataFrame = pd.read_csv(f'{DATASETS_PATH}final_temperature.csv')

# Сельскохозяйственных культуры
crop_production_df: pd.DataFrame = pd.read_csv(f'{DATASETS_PATH}crop_production.csv')

# Урожайность
crop_yield_df: pd.DataFrame = pd.read_csv(f'{DATASETS_PATH}crop_yield.csv')


@app.get('/', response_class=PlainTextResponse)
def get_welcome_page() -> str:
    '''
    Возвращает сообщение для корневой страницы.
    '''
    return (f"Fast API работает!\n\n"
            "Список запросов:\n"
            "\t- /api/rainfall/all\n"
            "\t- /api/temperature/all\n"
            "\t- /api/crop_production/all\n"
            "\t- /api/crop_yield/all\n"
            "\t- /api/rainfall/state/{state}\n"
            "\t- /api/temperature/state/{state}\n"
            "\t- /api/crop_production/state/{state}\n"
            "\t- /api/crop_yield/state/{state}\n")


@app.get('/api/rainfall/all')
def get_all_rainfall() -> List[Dict]:
    '''
    Возвращает все осадки.
    '''
    return rainfall_df.to_dict(orient='records')


@app.get('/api/temperature/all')
def get_all_temperature() -> List[Dict]:
    '''
    Возвращает все температуры.
    '''
    return temperature_df.to_dict(orient='records')


@app.get('/api/crop_production/all')
def get_all_crop_production() -> List[Dict]:
    '''
    Возвращает все культуры.
    '''
    return crop_production_df.to_dict(orient='records')


@app.get('/api/crop_yield/all')
def get_all_crop_yield() -> List[Dict]:
    '''
    Возвращает все записи по урожаю.
    '''
    return crop_yield_df.to_dict(orient='records')


@app.get('/api/rainfall/state/{state}')
def get_rainfall_by_state(state: str) -> List[Dict]:
    '''
    Возвращает осадки для территории.
    '''
    data = rainfall_df[rainfall_df['states'] == state]
    return data.to_dict(orient='records')


@app.get('/api/temperature/state/{state}')
def get_temperature_by_state(state: str) -> List[Dict]:
    '''
    Возвращает температуры для территории.
    '''
    data = temperature_df[temperature_df['state'] == state]
    return data.to_dict(orient='records')


@app.get('/api/crop_production/state/{state}')
def get_crop_production_by_state(state: str) -> List[Dict]:
    '''
    Возвращает культуры для территории.
    '''
    data = crop_production_df[crop_production_df['state_Name'] == state]
    return data.to_dict(orient='records')


@app.get('/api/crop_yield/district/{district}')
def get_crop_yield_by_district(district: str) -> List[Dict]:
    '''
    Возвращает урожай для территории.
    '''
    data = crop_yield_df[crop_yield_df['district_Name'] == district]
    return data.to_dict(orient='records')
