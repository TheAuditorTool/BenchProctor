# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest28885(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = header_value if header_value else 'default'
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
