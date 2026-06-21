# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest10182(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
