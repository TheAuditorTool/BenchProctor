# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest17475(request: Request):
    host_value = request.headers.get('host', '')
    data = ensure_str(host_value)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
