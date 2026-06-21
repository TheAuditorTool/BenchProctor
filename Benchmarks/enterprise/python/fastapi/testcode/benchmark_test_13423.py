# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest13423(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    if os.environ.get("APP_ENV", "production") != "test":
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
