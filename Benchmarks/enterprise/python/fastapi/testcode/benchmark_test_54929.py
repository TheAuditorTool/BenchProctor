# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest54929(request: Request):
    user_id = request.query_params.get('id', '')
    data = default_blank(user_id)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
