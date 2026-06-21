# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest35612(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = RequestPayload(upload_name).value
    yaml.safe_load(data)
    return {"updated": True}
