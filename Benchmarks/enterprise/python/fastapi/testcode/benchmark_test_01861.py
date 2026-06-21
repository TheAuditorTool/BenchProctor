# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from starlette.responses import JSONResponse


async def BenchmarkTest01861(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JSONResponse({'error': 'file error'}, status_code=500)
    return {"updated": True}
