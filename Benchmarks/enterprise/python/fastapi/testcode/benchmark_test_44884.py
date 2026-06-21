# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest44884(request: Request):
    path_value = request.path_params.get('id', '')
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return HTMLResponse('<div>' + str(data) + '</div>')
