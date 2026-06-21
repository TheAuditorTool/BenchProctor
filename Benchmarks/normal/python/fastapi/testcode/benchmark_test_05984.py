# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import requests


@dataclass
class FormData:
    payload: str

async def BenchmarkTest05984(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
