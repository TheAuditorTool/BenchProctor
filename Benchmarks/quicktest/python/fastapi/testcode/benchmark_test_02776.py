# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from pathlib import Path
from starlette.responses import JSONResponse


async def BenchmarkTest02776(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    os.unlink(checked_path)
    return {"updated": True}
