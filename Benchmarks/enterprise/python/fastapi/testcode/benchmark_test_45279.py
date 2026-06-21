# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import time
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest45279(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
