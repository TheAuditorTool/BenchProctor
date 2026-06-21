# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest50611(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})
