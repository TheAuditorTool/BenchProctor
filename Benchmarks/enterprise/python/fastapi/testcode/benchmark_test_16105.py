# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
from fastapi import Form


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest16105(request: Request, field: str = Form('')):
    field_value = field
    data = RequestPayload(field_value).value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
