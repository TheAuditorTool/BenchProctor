# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest38427(request: Request):
    user_id = request.query_params.get('id', '')
    data = '{}'.format(user_id)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
