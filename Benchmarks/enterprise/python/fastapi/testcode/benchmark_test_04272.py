# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest04272(request: Request):
    path_value = request.path_params.get('id', '')
    data = ' '.join(str(path_value).split())
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
