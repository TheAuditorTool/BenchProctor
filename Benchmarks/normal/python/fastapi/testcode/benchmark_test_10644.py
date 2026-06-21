# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket
from app_runtime import db


async def BenchmarkTest10644(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
