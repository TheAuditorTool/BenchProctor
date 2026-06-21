# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest17507(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = default_blank(comment_value)
    _ev = {}
    eval(compile("_ev['r'] = HTMLResponse('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']
