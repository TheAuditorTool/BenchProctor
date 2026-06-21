# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
from app_runtime import db


async def BenchmarkTest09825(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
