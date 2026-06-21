# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest13140(request: Request):
    path_value = request.path_params.get('id', '')
    data = normalise_input(path_value)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
