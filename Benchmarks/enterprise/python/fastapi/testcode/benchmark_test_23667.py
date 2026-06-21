# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest23667(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return JSONResponse({'error': 'privilege drop failed'}, status_code=500)
    return {"updated": True}
