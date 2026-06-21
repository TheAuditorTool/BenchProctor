# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from dataclasses import dataclass
import os
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest13199(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
