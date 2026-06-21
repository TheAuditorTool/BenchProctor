# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time
import subprocess
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest09033(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ctx = RequestContext(db_value)
    data = ctx.payload
    if time.time() > 1000000000:
        subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
