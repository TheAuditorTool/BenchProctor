# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree
from app_runtime import db


async def BenchmarkTest66382(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
