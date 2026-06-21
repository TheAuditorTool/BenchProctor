# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest42345(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(xml_value))
    return resp
