# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest09037(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = coalesce_blank(forwarded_ip)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
