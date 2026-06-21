# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest63604(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
