# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest67159(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return JSONResponse({'error': 'privilege drop failed'}, status_code=500)
    return {"updated": True}
