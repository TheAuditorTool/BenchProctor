# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os
from app_runtime import db


async def BenchmarkTest05551(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
