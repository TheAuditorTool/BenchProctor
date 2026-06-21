# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest43399(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
