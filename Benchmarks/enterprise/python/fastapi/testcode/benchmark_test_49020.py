# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest49020(request: Request):
    path_value = request.path_params.get('id', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(path_value),))
    return {"updated": True}
