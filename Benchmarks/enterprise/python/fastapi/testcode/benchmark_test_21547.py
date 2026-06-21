# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest21547(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return {"updated": True}
