# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest37024(request: Request):
    path_value = request.path_params.get('id', '')
    db.execute('SELECT * FROM users WHERE id = ' + str(path_value))
    return {"updated": True}
