# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import tempfile
from app_runtime import db


async def BenchmarkTest49886(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data, _sep, _rest = str(comment_value).partition('\x00')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
