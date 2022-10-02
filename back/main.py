# from importlib.resources import path
# from pathlib import Path
# from winreg import QueryInfoKey
from typing import List, Optional
from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from fastapi import FastAPI, Path, APIRouter, HTTPException, Response

from routers.user_router import user_router


def create_app() -> FastAPI:
    app = FastAPI()(
        title='Тестовое приложение',
        version='0.0.1a',
    )

    app.include_router(user_router)

    return app


app = create_app()
# @app.get('/')
# def ping():
#     return 'pong'
#
#
# @app.get('/hello')
# def print_hello():
#     return {'msg': 'Hello, world!'}
#
#
# @app.get('/world')
# def print_hello():
#     return {'msg': 'World, hello!'}
#
#
# @app.get('/print/{something}')
# def print_something(something: int = Path(include_in_schema=False)):
#     return {'msg': f'Печатаю что-то: {something}'}
# http://127.0.0.1:8000/print?s=123
