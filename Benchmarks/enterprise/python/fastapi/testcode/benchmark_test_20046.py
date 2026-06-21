# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest20046(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = normalise_input(db_value)
    def _primary():
        subprocess.run([str(data), '--status'], shell=False)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
