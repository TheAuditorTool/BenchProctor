# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import time
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest53070(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
