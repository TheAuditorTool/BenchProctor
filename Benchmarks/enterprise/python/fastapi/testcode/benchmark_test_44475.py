# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import HTMLResponse


async def BenchmarkTest44475(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    return HTMLResponse(str(data))
