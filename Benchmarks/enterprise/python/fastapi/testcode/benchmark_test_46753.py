# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from fastapi import Form
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest46753(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return {"updated": True}
