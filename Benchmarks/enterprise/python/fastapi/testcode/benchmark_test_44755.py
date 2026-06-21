# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest44755(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
