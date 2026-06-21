# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest23632(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    checked_path = os.path.join('/var/app/data', os.path.basename(db_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
