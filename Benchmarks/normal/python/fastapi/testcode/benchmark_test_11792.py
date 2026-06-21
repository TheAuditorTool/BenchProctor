# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest11792(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value}'
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
