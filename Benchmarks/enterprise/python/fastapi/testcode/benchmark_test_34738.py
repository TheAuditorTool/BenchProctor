# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest34738(request: Request):
    user_id = request.query_params.get('id', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(user_id)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = user_id
    values = str(processed).split(',')
    if values:
        return JSONResponse({'first': values[0], 'dropped': len(values) - 1}, status_code=200)
    return {"updated": True}
