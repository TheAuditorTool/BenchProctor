# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json
from app_runtime import db


async def BenchmarkTest55936(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
