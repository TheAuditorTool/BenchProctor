# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest47380(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = '%s' % str(comment_value)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
