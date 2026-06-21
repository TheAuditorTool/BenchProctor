# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest54850(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % str(multipart_value)
    if str(data) == 'is_admin':
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
