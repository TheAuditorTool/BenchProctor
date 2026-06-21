# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, auth_check


async def BenchmarkTest75154(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = str(comment_value).replace('\x00', '')
    auth_check('user', data)
    return {"updated": True}
