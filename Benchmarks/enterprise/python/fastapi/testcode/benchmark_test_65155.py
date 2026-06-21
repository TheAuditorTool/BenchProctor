# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest65155(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return {"updated": True}
