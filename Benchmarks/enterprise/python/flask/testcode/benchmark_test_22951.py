# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import asyncio
from types import SimpleNamespace
from app_runtime import db


def BenchmarkTest22951():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
