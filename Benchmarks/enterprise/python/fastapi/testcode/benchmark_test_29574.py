# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest29574(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    try:
        int(str(data))
    except ValueError:
        return JSONResponse({'error': 'invalid'}, status_code=400)
    return {"updated": True}
