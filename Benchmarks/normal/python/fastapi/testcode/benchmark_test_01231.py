# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest01231(request: Request):
    path_value = request.path_params.get('id', '')
    data = path_value if path_value else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
