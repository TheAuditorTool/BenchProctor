# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from app_runtime import db


async def BenchmarkTest08923(request: Request):
    ua_value = request.headers.get('user-agent', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(ua_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = ua_value
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return {"updated": True}
