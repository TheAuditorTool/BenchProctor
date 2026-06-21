# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import defusedxml.ElementTree
from app_runtime import db


async def BenchmarkTest66482(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
