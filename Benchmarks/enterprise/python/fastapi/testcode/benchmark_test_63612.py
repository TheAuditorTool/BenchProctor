# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest63612(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = '%s' % str(raw_body)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
