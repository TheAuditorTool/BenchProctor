# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest43696(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
