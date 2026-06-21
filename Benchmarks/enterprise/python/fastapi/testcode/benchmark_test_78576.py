# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest78576(request: Request):
    origin_value = request.headers.get('origin', '')
    data = normalise_input(origin_value)
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
