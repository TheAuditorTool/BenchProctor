# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def ensure_str(value):
    return str(value)

async def BenchmarkTest31569(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ensure_str(comment_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
