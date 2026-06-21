# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pathlib import Path
from starlette.responses import JSONResponse


async def BenchmarkTest79568(request: Request):
    user_id = request.query_params.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return {"updated": True}
