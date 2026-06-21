# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db, auth_check


async def BenchmarkTest79300(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(comment_value)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
