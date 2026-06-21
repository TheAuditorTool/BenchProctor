# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest70725(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ensure_str(forwarded_ip)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
