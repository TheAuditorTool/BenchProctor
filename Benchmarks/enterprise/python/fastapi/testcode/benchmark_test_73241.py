# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest73241(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = default_blank(db_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
