# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


async def BenchmarkTest67799(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
