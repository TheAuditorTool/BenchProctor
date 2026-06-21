# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest00622(request: Request):
    path_value = request.path_params.get('id', '')
    data = relay_value(path_value)
    if not re.fullmatch("^[\\w\\s.'\\\\;_/\\-]+$", data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
