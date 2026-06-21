# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest09965(request: Request):
    user_id = request.query_params.get('id', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(user_id),))
    return {"updated": True}
