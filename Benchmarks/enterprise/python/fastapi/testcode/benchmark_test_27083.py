# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest27083(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
