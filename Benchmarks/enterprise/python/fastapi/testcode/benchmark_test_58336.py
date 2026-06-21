# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import json
import os
from app_runtime import db


async def BenchmarkTest58336(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
