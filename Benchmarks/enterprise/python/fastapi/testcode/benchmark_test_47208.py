# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree
from app_runtime import db


async def BenchmarkTest47208(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
