# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from app_runtime import db


async def BenchmarkTest31801(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
