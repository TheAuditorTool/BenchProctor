# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest56545(request: Request):
    user_id = request.query_params.get('id', '')
    return JSONResponse({'error': str(user_id), 'stack': repr(locals())}, status_code=500)
