# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest16739(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        os.setuid(int(str(upload_name)) if str(upload_name).isdigit() else 65534)
    except OSError:
        return JSONResponse({'error': 'privilege drop failed'}, status_code=500)
    return {"updated": True}
