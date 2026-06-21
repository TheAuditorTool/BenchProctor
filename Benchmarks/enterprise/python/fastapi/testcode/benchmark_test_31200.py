# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest31200(request: Request):
    referer_value = request.headers.get('referer', '')
    data = str(referer_value).replace('\x00', '')
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JSONResponse({'error': 'file error'}, status_code=500)
    return {"updated": True}
