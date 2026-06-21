# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest47029(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
