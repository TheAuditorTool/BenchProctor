# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest09328(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '{}'.format(multipart_value)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
