# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest40231(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    prefix = ''
    data = prefix + str(header_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
