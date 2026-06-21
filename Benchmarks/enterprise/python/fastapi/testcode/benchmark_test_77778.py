# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote


async def BenchmarkTest77778(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
