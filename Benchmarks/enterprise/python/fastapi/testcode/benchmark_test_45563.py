# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest45563(request: Request):
    user_id = request.query_params.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
