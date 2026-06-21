# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest01684(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
