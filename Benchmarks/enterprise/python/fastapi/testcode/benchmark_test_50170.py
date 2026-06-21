# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest50170(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
