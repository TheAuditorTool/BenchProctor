# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest76334(request: Request):
    path_value = request.path_params.get('id', '')
    data = (lambda v: v.strip())(path_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
