# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest72657(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
