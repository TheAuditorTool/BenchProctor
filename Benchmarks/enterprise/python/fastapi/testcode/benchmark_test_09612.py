# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest09612(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    values = str(data).split(',')
    if values:
        return JSONResponse({'first': values[0], 'dropped': len(values) - 1}, status_code=200)
    return {"updated": True}
