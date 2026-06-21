# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from app_runtime import db


async def BenchmarkTest38623(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value}'
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
