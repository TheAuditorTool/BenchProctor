# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest62224(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
