# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest60573(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    return RedirectResponse(url=str(data))
