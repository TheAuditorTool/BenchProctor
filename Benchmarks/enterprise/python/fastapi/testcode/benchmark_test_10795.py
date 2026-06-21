# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest10795(request: Request):
    upload_name = (await request.form()).get('upload', '')
    requests.post('https://api.prod.internal/data', data=str(upload_name), verify=True)
    return {"updated": True}
