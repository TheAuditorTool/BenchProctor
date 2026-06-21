# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os
from app_runtime import db


async def BenchmarkTest21089(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(db_value))
    return {"updated": True}
