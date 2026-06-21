# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest04414(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = relay_value(ua_value)
    processed = data[:64]
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
