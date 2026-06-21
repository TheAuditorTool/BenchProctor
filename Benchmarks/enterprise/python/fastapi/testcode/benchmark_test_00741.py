# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest00741(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ensure_str(db_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
