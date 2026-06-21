# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest10130(request: Request):
    upload_name = request.query_params.get('filename', '')
    if upload_name:
        data = upload_name
    else:
        data = ''
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return JSONResponse({'error': 'invalid file type'}, status_code=400)
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
