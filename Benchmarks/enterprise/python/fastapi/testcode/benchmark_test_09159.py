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

async def BenchmarkTest09159(request: Request):
    path_value = request.path_params.get('id', '')
    data = RequestPayload(path_value).value
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
