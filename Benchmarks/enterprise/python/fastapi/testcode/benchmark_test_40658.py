# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest40658(request: Request, field: str = Form('')):
    field_value = field
    prefix = ''
    data = prefix + str(field_value)
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
