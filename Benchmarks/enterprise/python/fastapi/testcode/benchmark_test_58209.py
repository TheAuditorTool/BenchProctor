# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from app_runtime import db


async def BenchmarkTest58209(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
