# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse


async def BenchmarkTest63874(request: Request):
    user_id = request.query_params.get('id', '')
    return HTMLResponse('<div>' + str(user_id) + '</div>')
