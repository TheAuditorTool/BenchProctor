# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import time
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest46796(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    ns = SimpleNamespace(payload=db_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        return HTMLResponse(Template(data).render())
    return {"updated": True}
