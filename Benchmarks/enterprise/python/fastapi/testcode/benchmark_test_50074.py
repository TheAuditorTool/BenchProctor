# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest50074(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
