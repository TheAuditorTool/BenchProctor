# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db, auth_check


async def BenchmarkTest13574(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    auth_check('user', data)
    return {"updated": True}
