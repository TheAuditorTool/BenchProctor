# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest07887(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ensure_str(origin_value)
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JSONResponse({'error': 'file error'}, status_code=500)
    return {"updated": True}
