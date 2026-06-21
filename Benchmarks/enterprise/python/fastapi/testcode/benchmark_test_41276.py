# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from urllib.parse import unquote


async def BenchmarkTest41276(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
