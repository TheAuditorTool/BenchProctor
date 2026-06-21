# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from urllib.parse import unquote


async def BenchmarkTest51119(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    return HTMLResponse('<div>' + str(data) + '</div>')
