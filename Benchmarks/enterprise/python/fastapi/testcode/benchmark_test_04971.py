# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest04971(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
