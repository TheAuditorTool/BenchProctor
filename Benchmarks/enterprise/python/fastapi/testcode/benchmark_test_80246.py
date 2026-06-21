# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from fastapi import Form


async def BenchmarkTest80246(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % (field_value,)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
