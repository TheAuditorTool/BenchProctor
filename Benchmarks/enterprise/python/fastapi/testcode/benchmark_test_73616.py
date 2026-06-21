# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest73616(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
