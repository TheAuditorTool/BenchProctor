# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, auth_check


async def BenchmarkTest08389(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    kind = 'json' if str(comment_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = comment_value
            data = parsed
        case _:
            data = comment_value
    auth_check('user', data)
    return {"updated": True}
