# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest36729(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '%s' % str(header_value)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
