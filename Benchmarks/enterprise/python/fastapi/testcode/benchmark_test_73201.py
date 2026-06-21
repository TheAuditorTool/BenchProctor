# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest73201(request: Request):
    path_value = request.path_params.get('id', '')
    data = str(path_value).replace('\x00', '')
    values = str(data).split(',')
    if values:
        return JSONResponse({'first': values[0], 'dropped': len(values) - 1}, status_code=200)
    return {"updated": True}
