# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys
from app_runtime import db


async def BenchmarkTest03845(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
