# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from app_runtime import db


async def BenchmarkTest08604(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(comment_value)
    data = collected
    def _primary():
        subprocess.run('echo ' + str(data), shell=True)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
