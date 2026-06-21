# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from urllib.parse import unquote


async def BenchmarkTest11329(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    return HTMLResponse('<div>' + str(data) + '</div>')
