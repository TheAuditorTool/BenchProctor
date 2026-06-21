# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest73741(request: Request):
    upload_name = (await request.form()).get('upload', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': str(data)})
