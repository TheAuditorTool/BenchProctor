# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest75664(request: Request):
    origin_value = request.headers.get('origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
