"""
 Copyright 2023 Google LLC

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 """

"""DB connection definition."""
import os

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

# Obtiene la URL de conexión de la variable de entorno
database_url = os.environ.get('CONFIG_DB_CONN')

# Crea el motor asíncrono directamente
engine = create_async_engine(database_url, echo=True, future=True)


async def get_session() -> AsyncSession:
  async_session = sessionmaker(
      engine, class_=AsyncSession, expire_on_commit=False
  )
  async with async_session() as session:
    yield session
