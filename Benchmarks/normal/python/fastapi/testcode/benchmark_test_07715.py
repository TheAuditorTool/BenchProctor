# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest07715(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
