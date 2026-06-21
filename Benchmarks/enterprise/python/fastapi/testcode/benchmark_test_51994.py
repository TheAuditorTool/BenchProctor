# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest51994(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    random.seed(int(multipart_value) if str(multipart_value).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
