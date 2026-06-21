# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest46857(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
