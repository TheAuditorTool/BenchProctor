# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest07892(request: Request):
    upload_name = (await request.form()).get('upload', '')
    requests.get(str(upload_name))
    return {"updated": True}
