# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest35305(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = FormData(payload=auth_header).payload
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
