# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import sys
from starlette.responses import JSONResponse


async def BenchmarkTest18338(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = '%s' % str(argv_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('/var/app/data/' + str(processed), 'w') as fh:
        fh.write('data')
    return {"updated": True}
