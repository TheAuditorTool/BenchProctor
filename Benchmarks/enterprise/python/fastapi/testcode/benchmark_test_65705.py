# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree
from app_runtime import db


async def BenchmarkTest65705(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    defusedxml.ElementTree.fromstring(str(db_value))
    return {"updated": True}
