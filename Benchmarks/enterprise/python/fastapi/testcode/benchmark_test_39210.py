# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from starlette.responses import JSONResponse


async def BenchmarkTest39210(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return JSONResponse({'error': 'invalid file type'}, status_code=400)
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
