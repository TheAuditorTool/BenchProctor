# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from starlette.responses import JSONResponse


async def BenchmarkTest03790(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '{}'.format(upload_name)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)
