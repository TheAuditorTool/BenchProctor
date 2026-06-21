# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest49137(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
