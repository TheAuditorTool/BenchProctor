# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest11099(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
