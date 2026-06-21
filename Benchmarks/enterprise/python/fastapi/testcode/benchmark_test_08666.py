# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pathlib import Path
import os
from starlette.responses import JSONResponse


async def BenchmarkTest08666(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    base = Path('/var/app/data').resolve()
    candidate = (base / env_value).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return {"updated": True}
