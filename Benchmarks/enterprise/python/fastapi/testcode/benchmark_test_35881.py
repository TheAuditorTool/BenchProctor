# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from urllib.parse import unquote


async def BenchmarkTest35881(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
