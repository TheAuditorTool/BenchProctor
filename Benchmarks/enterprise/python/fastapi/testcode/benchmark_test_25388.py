# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import HTMLResponse
from app_runtime import db


async def BenchmarkTest25388(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = '%s' % str(db_value)
    return HTMLResponse('<script src="' + str(data) + '"></script>')
