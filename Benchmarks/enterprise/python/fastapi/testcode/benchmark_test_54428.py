# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest54428(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = RequestPayload(upload_name).value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
