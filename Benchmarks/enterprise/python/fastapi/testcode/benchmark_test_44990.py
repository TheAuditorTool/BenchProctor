# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import base64


async def BenchmarkTest44990(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
