# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest45593(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '%s' % (forwarded_ip,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
