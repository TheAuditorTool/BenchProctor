# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest43533(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    if str(data) == 'fluffy':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
