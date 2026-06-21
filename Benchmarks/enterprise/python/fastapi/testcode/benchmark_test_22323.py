# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest22323(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ensure_str(header_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
