# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest22685(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    requests.post('https://api.prod.internal/data', data=str(db_value), verify=True)
    return {"updated": True}
