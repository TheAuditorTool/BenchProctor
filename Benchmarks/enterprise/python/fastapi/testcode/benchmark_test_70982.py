# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import socket
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest70982(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = FormData(payload=db_value).payload
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
