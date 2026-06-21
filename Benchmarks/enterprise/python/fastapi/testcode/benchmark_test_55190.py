# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from app_runtime import db


async def BenchmarkTest55190(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
