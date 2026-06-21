# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import tempfile
from app_runtime import db


async def BenchmarkTest07232(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
