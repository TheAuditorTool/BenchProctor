# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


async def BenchmarkTest28944(request: Request):
    referer_value = request.headers.get('referer', '')
    processed = bleach.clean(referer_value)
    return HTMLResponse('<div>' + str(processed) + '</div>')
