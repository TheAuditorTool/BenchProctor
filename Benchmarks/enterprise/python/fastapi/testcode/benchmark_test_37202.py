# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from app_runtime import db


async def BenchmarkTest37202(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    processed = data[:64]
    globals()['counter'] = int(processed)
    return {"updated": True}
