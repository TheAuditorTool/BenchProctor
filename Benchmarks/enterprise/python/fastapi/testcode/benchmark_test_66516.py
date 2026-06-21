# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os
from app_runtime import db


async def BenchmarkTest66516(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
