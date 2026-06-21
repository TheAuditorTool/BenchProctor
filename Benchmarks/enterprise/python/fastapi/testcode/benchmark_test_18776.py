# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest18776(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
