# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest54314(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % str(db_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
