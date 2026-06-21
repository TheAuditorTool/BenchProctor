# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest44444(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    return HTMLResponse(str(data))
