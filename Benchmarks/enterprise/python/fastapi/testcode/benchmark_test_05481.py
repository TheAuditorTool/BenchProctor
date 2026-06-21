# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest05481(request: Request):
    auth_header = request.headers.get('authorization', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', auth_header):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = auth_header
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
