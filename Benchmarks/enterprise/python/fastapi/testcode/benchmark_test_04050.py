# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from app_runtime import db


async def BenchmarkTest04050(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = f'{db_value:.200s}'
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
