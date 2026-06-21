# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import asyncio
from app_runtime import db


def BenchmarkTest25810():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        return Markup('<div>' + str(data) + '</div>')
    return asyncio.run(_evasion_task())
