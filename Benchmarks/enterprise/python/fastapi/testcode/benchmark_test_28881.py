# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest28881(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ensure_str(multipart_value)
    return HTMLResponse(str(data))
