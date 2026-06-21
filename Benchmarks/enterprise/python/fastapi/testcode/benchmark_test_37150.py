# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest37150(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with open('/var/uploads/' + str(comment_value), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
