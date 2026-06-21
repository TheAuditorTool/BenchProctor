# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import os
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest80747(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
