# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


async def BenchmarkTest80713(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
