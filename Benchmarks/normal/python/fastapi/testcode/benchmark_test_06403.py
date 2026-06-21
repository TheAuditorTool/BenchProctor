# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


async def BenchmarkTest06403(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(multipart_value)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = multipart_value
    eval(str(processed))
    return {"updated": True}
