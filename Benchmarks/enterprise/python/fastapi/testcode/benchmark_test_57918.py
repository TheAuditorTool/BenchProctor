# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest57918(request: Request):
    path_value = request.path_params.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
