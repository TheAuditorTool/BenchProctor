# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket
from app_runtime import db


async def BenchmarkTest34508(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    s = socket.create_connection((str(db_value), 80))
    s.close()
    return {"updated": True}
