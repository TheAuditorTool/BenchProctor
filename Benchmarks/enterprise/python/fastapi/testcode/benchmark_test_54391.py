# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest54391(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
