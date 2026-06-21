# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest34723(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return {"updated": True}
