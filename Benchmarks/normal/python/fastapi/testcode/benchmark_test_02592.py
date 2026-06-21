# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest02592(request: Request):
    ua_value = request.headers.get('user-agent', '')
    base_name = os.path.basename(str(ua_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
