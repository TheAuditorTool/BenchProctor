# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle
from app_runtime import db


async def BenchmarkTest61488(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    pickle.loads(db_value.encode('latin-1'))
    return {"updated": True}
