# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db, auth_check


async def BenchmarkTest18306(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(comment_value), store_cred)
    return {"updated": True}
