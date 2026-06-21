# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest21798(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
