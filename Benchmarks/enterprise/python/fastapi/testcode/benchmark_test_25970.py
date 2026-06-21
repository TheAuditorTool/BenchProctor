# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def to_text(value):
    return str(value).strip()

async def BenchmarkTest25970(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = to_text(upload_name)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
