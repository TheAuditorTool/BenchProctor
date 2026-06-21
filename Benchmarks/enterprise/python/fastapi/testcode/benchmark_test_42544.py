# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest42544(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    requests.get(str(db_value))
    return {"updated": True}
