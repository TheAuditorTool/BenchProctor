# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest77574(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    prefix = ''
    data = prefix + str(xml_value)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
