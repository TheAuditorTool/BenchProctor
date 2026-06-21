# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest56900(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
