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

async def BenchmarkTest30762(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = RequestPayload(upload_name).value
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
