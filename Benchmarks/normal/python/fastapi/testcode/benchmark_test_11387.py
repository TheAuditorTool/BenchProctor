# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest11387(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
