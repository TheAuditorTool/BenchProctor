# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest49266(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
