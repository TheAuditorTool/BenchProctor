# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest12248(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = '%s' % str(ua_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
