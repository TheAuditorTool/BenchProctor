# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest03008(request: Request):
    user_id = request.query_params.get('id', '')
    data = to_text(user_id)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    os.system('echo ' + str(processed))
    return {"updated": True}
