# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest60677(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return {"updated": True}
