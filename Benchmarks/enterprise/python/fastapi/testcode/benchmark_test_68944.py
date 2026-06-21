# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
import tempfile


async def BenchmarkTest68944(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
