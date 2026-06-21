# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pathlib import Path
from starlette.responses import JSONResponse


async def BenchmarkTest01023(request: Request):
    referer_value = request.headers.get('referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    os.unlink(checked_path)
    return {"updated": True}
