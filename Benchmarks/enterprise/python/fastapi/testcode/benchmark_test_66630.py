# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest66630(request: Request):
    referer_value = request.headers.get('referer', '')
    data = normalise_input(referer_value)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
