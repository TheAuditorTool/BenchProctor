# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest20183(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(multipart_value))
    return resp
