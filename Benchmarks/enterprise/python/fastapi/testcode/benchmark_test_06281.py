# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import requests


async def BenchmarkTest06281(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
