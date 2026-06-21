# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse


async def BenchmarkTest63401(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    return RedirectResponse(url=str(data))
