# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pathlib import Path
from fastapi import Form
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest10695(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
