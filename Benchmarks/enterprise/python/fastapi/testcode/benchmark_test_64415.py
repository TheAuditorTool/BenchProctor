# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest64415(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
