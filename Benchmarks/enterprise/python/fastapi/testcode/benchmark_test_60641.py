# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest60641(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
