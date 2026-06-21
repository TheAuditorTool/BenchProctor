# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from app_runtime import db, auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest81418(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    auth_check('user', data)
    return {"updated": True}
