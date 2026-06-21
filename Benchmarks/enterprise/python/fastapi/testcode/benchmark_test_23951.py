# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest23951(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}
