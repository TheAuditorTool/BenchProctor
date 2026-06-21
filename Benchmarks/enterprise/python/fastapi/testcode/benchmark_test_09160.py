# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest09160(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    entries = os.listdir(str(multipart_value))
    return JSONResponse({'listing': entries}, status_code=200)
