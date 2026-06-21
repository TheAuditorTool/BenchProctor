# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest29704(request: Request):
    upload_name = (await request.form()).get('upload', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(upload_name)}, verify=False)
    return {"updated": True}
