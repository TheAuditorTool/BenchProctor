# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree
from app_runtime import db


async def BenchmarkTest02082(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
