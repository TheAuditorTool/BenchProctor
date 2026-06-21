# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
from app_runtime import db


async def BenchmarkTest32624(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    importlib.import_module(str(data))
    return {"updated": True}
