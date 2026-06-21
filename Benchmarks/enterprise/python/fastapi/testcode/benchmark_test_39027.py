# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest39027(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    random.seed(int(multipart_value) if str(multipart_value).isdigit() else 99)
    token = random.randint(0, 99)
    return JSONResponse({'token': str(token)}, status_code=200)
