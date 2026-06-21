# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest20573(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data, _sep, _rest = str(xml_value).partition('\x00')
    if request.session.get('role') != 'admin':
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    request.session['data'] = str(data)
    return {"updated": True}
