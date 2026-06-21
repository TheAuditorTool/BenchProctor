# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest46649(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return {"updated": True}
