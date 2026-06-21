# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest44793(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    checked_path = os.path.join('/var/app/data', os.path.basename(comment_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
