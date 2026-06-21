# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import db, auth_check


async def BenchmarkTest00415(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
