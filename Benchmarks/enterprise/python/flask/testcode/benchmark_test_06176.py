# SPDX-License-Identifier: Apache-2.0
import os
import asyncio
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest06176():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        link_path = os.path.join('/var/app/data', str(data))
        target = os.readlink(link_path)
        with open(target, 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
