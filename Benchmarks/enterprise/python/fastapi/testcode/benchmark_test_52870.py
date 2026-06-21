# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html


async def BenchmarkTest52870(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
