# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pathlib import Path
import os
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest12498(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
