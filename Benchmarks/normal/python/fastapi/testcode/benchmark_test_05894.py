# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest05894(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
