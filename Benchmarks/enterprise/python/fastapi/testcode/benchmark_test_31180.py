# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest31180(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    processed = html.escape(multipart_value)
    return HTMLResponse('<img src="' + str(processed) + '">')
