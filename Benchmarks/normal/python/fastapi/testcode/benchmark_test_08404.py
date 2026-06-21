# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest08404(request: Request):
    path_value = request.path_params.get('id', '')
    data = '%s' % str(path_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
