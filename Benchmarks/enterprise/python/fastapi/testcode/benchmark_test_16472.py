# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest16472(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(multipart_value)
    if origin in allowed:
        return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': origin})
    return {"updated": True}
