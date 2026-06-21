# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest04513(request: Request):
    host_value = request.headers.get('host', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(host_value),))
    return {"updated": True}
