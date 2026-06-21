# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest17106(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    return HTMLResponse('<div>' + str(data) + '</div>')
