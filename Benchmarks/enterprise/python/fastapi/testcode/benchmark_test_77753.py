# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest77753(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(upload_name)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = upload_name
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HTMLResponse('<p>' + normalized + '</p>')
