# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest58094(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = RequestPayload(upload_name).value
    requests.get(str(data))
    return {"updated": True}
