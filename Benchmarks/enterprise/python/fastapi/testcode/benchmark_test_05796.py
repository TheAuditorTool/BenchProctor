# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest05796(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JSONResponse({'error': 'file error'}, status_code=500)
    return {"updated": True}
