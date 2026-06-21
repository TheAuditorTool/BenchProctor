# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest72905(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    return RedirectResponse(url=str(data))
