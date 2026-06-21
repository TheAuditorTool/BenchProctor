# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest03957(request: Request):
    path_value = request.path_params.get('id', '')
    try:
        os.setuid(int(str(path_value)) if str(path_value).isdigit() else 65534)
    except OSError:
        return JSONResponse({'error': 'privilege drop failed'}, status_code=500)
    return {"updated": True}
