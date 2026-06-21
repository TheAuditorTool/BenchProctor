# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import re
from starlette.responses import JSONResponse


async def BenchmarkTest01426(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', upload_name):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = upload_name
    return HTMLResponse('<img src="' + str(processed) + '">')
