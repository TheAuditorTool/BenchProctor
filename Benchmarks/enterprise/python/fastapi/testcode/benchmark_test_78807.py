# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest78807(request: Request):
    user_id = request.query_params.get('id', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(user_id))
    return resp
