# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest41523(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return JSONResponse({'record': str(record)}, status_code=200)
