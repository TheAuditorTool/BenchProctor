# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, auth_check


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest13045(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    auth_check('user', data)
    return {"updated": True}
