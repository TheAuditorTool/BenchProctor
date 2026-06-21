# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import requests
from starlette.responses import JSONResponse
from types import SimpleNamespace


async def BenchmarkTest80633(request: Request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    ns = SimpleNamespace(payload=api_value)
    data = getattr(ns, 'payload')
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not data.lower().endswith(allowed_ext):
        return JSONResponse({'error': 'invalid file type'}, status_code=400)
    entry_file = os.path.basename(data)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}
