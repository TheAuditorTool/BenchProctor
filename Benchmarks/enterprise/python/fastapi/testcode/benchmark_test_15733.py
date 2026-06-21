# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
import os
from types import SimpleNamespace


async def BenchmarkTest15733(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
