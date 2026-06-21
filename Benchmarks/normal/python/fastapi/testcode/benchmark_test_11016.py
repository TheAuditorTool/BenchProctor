# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest11016(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
