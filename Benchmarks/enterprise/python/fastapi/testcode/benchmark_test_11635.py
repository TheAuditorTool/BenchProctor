# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import socket
from app_runtime import db


async def BenchmarkTest11635(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ' '.join(str(comment_value).split())
    s = socket.create_connection((str(data), 80))
    s.close()
    return {"updated": True}
