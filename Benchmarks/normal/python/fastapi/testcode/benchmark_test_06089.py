# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest06089(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
