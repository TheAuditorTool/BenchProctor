# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest02516(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    db.execute('SELECT * FROM users WHERE id = ' + str(header_value))
    return {"updated": True}
