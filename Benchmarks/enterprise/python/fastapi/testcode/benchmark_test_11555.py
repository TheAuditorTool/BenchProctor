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

async def BenchmarkTest11555(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
