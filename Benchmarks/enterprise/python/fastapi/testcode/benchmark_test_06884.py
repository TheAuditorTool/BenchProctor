# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest06884(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
