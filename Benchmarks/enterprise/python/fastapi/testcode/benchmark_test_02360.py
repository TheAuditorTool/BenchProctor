# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest02360(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(header_value)))
    return {"updated": True}
