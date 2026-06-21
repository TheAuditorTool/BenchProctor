# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest05350(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '%s' % (header_value,)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
