# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote


async def BenchmarkTest72152(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
