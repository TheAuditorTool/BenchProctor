# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest58659(request: Request):
    host_value = request.headers.get('host', '')
    data = ensure_str(host_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
