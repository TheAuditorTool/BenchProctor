# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest61742(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    processed = data[:64]
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(processed),))
    return JSONResponse({'record': str(record)}, status_code=200)
