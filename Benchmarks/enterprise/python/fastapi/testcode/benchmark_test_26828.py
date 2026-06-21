# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest26828(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
