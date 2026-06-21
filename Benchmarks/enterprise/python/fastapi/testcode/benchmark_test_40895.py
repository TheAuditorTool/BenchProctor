# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree
from app_runtime import db


async def BenchmarkTest40895(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = db_value if db_value else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
