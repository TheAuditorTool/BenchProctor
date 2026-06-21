# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest23976(request: Request):
    upload_name = (await request.form()).get('upload', '')
    random.seed(int(upload_name) if str(upload_name).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
