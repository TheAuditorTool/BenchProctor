# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest13352(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    os.remove(str(data))
    return {"updated": True}
