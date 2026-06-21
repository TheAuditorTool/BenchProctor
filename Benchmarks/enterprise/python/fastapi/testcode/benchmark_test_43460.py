# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest43460(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
