# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest07870(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    return HTMLResponse(str(data))
