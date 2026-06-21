# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest13774(request: Request):
    path_value = request.path_params.get('id', '')
    data = relay_value(path_value)
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
