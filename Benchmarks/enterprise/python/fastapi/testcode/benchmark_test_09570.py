# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest09570(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(forwarded_ip),))
    return {"updated": True}
