# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest71764(request: Request):
    referer_value = request.headers.get('referer', '')
    data = ' '.join(str(referer_value).split())
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
