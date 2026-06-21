# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket
from app_runtime import db


async def BenchmarkTest79721(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
