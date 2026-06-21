# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import HTMLResponse
import unicodedata


async def BenchmarkTest50495(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    normalized = unicodedata.normalize('NFKC', str(data))
    return HTMLResponse('<p>' + normalized + '</p>')
