# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from app_runtime import db


async def BenchmarkTest56332(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    subprocess.run([str(db_value), '--status'], shell=False)
    return {"updated": True}
