# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest22073(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
