# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest07388(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = RequestPayload(upload_name).value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
