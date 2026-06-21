# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest58100(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if upload_name:
        data = upload_name
    else:
        data = ''
    random.seed(int(data) if str(data).isdigit() else 1337)
    token = random.randint(0, 100000)
    return JSONResponse({'token': str(token)}, status_code=200)
