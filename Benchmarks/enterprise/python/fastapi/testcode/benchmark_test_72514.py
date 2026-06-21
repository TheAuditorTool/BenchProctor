# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest72514(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JSONResponse({'error': 'file error'}, status_code=500)
    return {"updated": True}
