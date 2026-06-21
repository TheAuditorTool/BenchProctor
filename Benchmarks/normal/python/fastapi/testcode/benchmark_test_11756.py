# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest11756(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
