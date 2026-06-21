# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest01116(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    db.execute('UPDATE users SET name = ?', (str(data),))
    return {"updated": True}
