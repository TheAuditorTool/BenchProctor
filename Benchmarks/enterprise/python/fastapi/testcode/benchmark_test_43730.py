# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse
import subprocess


async def BenchmarkTest43730(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', multipart_value):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = multipart_value
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}
