# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pathlib import Path
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest26148(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
