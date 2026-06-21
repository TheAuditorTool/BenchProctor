# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def to_text(value):
    return str(value).strip()

async def BenchmarkTest04496(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    def _primary():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
