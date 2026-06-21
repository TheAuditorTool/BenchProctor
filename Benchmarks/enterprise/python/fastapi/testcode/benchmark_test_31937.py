# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest31937(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    return HTMLResponse('<script src="' + str(comment_value) + '"></script>')
