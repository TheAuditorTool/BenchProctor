# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import sys


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

async def BenchmarkTest79253(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = RequestPayload(argv_value).value
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return {"updated": True}
