# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest11905(request: Request):
    host_value = request.headers.get('host', '')
    data = coalesce_blank(host_value)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
