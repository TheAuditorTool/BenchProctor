# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest62816(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = to_text(auth_header)
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JSONResponse({'error': 'file error'}, status_code=500)
    return {"updated": True}
