# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest24833(request: Request):
    path_value = request.path_params.get('id', '')
    data = default_blank(path_value)
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
