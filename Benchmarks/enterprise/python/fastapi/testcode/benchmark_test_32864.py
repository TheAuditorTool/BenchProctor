# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import db, auth_check


async def BenchmarkTest32864(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
