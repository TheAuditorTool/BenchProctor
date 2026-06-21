# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest27832(request: Request):
    upload_name = (await request.form()).get('upload', '')
    entries = os.listdir(str(upload_name))
    return JSONResponse({'listing': entries}, status_code=200)
