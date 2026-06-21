# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from app_runtime import db


async def BenchmarkTest76735(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
