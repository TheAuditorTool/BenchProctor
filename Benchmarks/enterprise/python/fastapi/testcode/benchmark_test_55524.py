# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from app_runtime import db, auth_check


async def BenchmarkTest55524(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return {"updated": True}
