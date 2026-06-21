# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from app_runtime import db


async def BenchmarkTest22750(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    yaml.safe_load(db_value)
    return {"updated": True}
