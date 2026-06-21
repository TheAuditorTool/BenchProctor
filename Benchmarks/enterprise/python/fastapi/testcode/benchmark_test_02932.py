# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest02932(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
