# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest01077(request: Request):
    path_value = request.path_params.get('id', '')
    data = ensure_str(path_value)
    if not re.fullmatch("^[\\w\\s.'\\\\;_/\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
