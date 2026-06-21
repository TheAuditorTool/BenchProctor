# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest73975(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % (db_value,)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
