# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest10873(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return JSONResponse({'error': 'privilege drop failed'}, status_code=500)
    return {"updated": True}
