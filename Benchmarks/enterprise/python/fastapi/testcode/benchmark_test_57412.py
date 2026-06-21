# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from app_runtime import db


async def BenchmarkTest57412(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
