# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pathlib import Path
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest01055(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
