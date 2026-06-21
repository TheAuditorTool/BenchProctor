# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest18789(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return {"updated": True}
