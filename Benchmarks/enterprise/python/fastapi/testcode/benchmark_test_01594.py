# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest01594(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(comment_value))
    return {"updated": True}
