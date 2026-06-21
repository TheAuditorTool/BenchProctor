# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from starlette.responses import JSONResponse


async def BenchmarkTest77811(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    if request.session.get('role') != 'admin':
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    request.session['data'] = str(data)
    return {"updated": True}
