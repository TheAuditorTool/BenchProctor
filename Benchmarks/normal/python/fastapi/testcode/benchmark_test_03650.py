# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest03650(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return {"updated": True}
