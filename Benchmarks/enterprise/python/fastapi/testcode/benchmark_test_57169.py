# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


async def BenchmarkTest57169(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    with open('/var/app/data/' + str(comment_value), 'r') as fh:
        content = fh.read()
    return content
