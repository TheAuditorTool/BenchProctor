# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest59988(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    yaml.safe_load(data)
    return {"updated": True}
