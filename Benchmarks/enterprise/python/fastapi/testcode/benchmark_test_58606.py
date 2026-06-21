# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest58606(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return {"updated": True}
