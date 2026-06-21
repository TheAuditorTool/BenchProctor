# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest20201(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
