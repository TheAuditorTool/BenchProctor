# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest71509(request: Request):
    path_value = request.path_params.get('id', '')
    data, _sep, _rest = str(path_value).partition('\x00')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HTMLResponse('<p>' + normalized + '</p>')
