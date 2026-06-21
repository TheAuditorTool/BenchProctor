# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import re
from starlette.responses import JSONResponse


async def BenchmarkTest11072(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % (multipart_value,)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JSONResponse({'error': 'invalid input'}, status_code=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
