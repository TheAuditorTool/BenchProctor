# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest12812(request: Request):
    origin_value = request.headers.get('origin', '')
    data = RequestPayload(origin_value).value
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
