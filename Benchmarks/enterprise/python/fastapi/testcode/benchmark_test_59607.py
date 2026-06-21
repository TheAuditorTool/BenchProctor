# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest59607(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    db.execute('SELECT * FROM users WHERE id = :id', {'id': data})
    return {"updated": True}
