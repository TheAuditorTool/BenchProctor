# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest00067(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
