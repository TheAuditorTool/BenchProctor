# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest25323(request: Request):
    host_value = request.headers.get('host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    values = str(data).split(',')
    if values:
        return JSONResponse({'first': values[0], 'dropped': len(values) - 1}, status_code=200)
    return {"updated": True}
