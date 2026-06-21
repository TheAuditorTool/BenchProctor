# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest39965(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        os.setuid(int(str(ua_value)) if str(ua_value).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
