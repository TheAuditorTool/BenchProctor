# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach


async def BenchmarkTest29500(request: Request):
    user_id = request.query_params.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
