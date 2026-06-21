# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest09042(request: Request):
    user_id = request.query_params.get('id', '')
    return RedirectResponse(url=str(user_id))
