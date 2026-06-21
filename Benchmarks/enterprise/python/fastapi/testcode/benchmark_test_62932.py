# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest62932(request: Request):
    origin_value = request.headers.get('origin', '')
    base_name = os.path.basename(str(origin_value))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JSONResponse({'error': 'file error'}, status_code=500)
    return {"updated": True}
