# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest11580(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body:.200s}'
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JSONResponse({'error': 'file error'}, status_code=500)
    return {"updated": True}
