# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest34655(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = default_blank(comment_value)
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return JSONResponse({'error': 'invalid file type'}, status_code=400)
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
