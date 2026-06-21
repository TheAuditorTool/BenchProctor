# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import asyncio
from app_runtime import db


async def BenchmarkTest42410(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return comment_value
    data = await fetch_payload()
    _ev = {}
    eval(compile("_ev['r'] = HTMLResponse(Template(data).render())", '<sink>', 'exec'))
    return _ev['r']
