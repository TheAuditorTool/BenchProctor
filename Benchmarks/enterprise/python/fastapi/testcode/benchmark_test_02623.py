# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pathlib import Path
from starlette.responses import JSONResponse


async def BenchmarkTest02623(request: Request):
    path_value = request.path_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
