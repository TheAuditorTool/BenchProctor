# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest69367(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
