# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest46435(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return JSONResponse({'error': 'zero division'}, status_code=400)
    result = 100 / divisor
    return {"updated": True}
