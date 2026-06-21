# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest52049(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    resp = JSONResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
