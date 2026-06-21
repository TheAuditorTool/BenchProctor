# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest60020(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
