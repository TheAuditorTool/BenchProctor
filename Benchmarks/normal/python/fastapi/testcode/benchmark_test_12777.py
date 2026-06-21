# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from starlette.responses import JSONResponse


async def BenchmarkTest12777(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '{}'.format(upload_name)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
