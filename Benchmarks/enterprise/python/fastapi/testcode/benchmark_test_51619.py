# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest51619(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = coalesce_blank(comment_value)
    def _primary():
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()
