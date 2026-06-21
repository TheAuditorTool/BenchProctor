# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest03590(request: Request):
    referer_value = request.headers.get('referer', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(referer_value),))
    return {"updated": True}
