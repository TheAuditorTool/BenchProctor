# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import sys
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest09480(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = normalise_input(argv_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return {"updated": True}
