# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest04745(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
