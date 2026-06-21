# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db, auth_check


async def BenchmarkTest58794(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    auth_check('user', data)
    return {"updated": True}
