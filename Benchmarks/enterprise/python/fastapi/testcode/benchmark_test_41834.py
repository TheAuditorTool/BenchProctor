# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest41834(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(multipart_value))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
