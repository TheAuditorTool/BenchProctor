# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest07444(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
