# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest02762(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    try:
        os.setuid(int(str(xml_value)) if str(xml_value).isdigit() else 65534)
    except OSError:
        return JSONResponse({'error': 'privilege drop failed'}, status_code=500)
    return {"updated": True}
