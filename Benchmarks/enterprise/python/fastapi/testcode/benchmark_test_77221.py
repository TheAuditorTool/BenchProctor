# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest77221(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if len(str(multipart_value)) >= 4:
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
