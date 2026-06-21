# SPDX-License-Identifier: Apache-2.0
import requests
import asyncio
from app_runtime import db


def BenchmarkTest18692():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = asyncio.run(fetch_payload())
    def _primary():
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
