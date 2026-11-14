from contextlib import asynccontextmanager
from typing import Annotated

import httpx
from fastapi import Depends, FastAPI, Query, Request
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):  
    model_config = SettingsConfigDict(env_file=".env")
    base_url: str = "https://jsonplaceholder.typicode.com"
    timeout: float = 5.0

settings = Settings()
