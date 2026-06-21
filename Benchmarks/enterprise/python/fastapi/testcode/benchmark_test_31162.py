# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest31162(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
