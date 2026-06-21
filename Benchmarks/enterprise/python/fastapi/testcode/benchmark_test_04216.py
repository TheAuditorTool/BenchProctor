# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest04216(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
