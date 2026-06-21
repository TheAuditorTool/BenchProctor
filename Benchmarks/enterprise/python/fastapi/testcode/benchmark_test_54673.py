# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import requests
from app_runtime import db


@dataclass
class FormData:
    payload: str

async def BenchmarkTest54673(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = FormData(payload=comment_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
