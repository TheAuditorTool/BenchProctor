# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from app_runtime import db


async def BenchmarkTest26117(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
