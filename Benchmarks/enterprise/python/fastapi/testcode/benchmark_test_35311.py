# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest35311(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '{}'.format(auth_header)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
