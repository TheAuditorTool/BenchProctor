# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest30988(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = relay_value(db_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
