# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest11999(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id}'
    return HTMLResponse(str(data))
