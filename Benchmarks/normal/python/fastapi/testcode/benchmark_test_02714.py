# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest02714(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
