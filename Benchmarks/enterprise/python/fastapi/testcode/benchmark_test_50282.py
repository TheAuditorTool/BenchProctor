# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest50282(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = upload_name if upload_name else 'default'
    if request.session.get('role') != 'admin':
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    request.session['data'] = str(data)
    return {"updated": True}
