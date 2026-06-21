# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest10147(request: Request):
    user_id = request.query_params.get('id', '')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, user_id))
    if not full_path.startswith(base_dir + os.sep):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
