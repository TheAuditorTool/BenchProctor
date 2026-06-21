# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from app_runtime import db


async def BenchmarkTest19903(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
