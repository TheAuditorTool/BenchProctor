# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest47262(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
