# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest10141(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    if len(str(data)) >= 4:
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
