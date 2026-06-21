# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from urllib.parse import unquote


async def BenchmarkTest05391(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
