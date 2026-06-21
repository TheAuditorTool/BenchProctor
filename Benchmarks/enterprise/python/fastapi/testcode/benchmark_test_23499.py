# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
import unicodedata


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest23499(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    normalized = unicodedata.normalize('NFKC', str(processed))
    return HTMLResponse('<p>' + normalized + '</p>')
