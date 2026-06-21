# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest21721(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = coalesce_blank(db_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
