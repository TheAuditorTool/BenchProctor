# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
import asyncio
from app_runtime import db


async def BenchmarkTest73984(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = await fetch_payload()
    def _primary():
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
