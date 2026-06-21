# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest68256(request: Request):
    host_value = request.headers.get('host', '')
    base_name = os.path.basename(str(host_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
