# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pathlib import Path
from dataclasses import dataclass
import sys
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest12973(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = FormData(payload=argv_value).payload
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return {"updated": True}
