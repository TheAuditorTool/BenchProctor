# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


def ensure_str(value):
    return str(value)

async def BenchmarkTest46155(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ensure_str(ua_value)
    processed = data[:64]
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return {"updated": True}
