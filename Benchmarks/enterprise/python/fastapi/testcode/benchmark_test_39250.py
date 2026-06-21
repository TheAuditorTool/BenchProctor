# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest39250(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
