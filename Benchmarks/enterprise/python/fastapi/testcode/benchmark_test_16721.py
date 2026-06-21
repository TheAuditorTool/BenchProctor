# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import socket
from app_runtime import db


async def BenchmarkTest16721(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = json.loads(db_value).get('value', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
