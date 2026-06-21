# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest39988(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    os.remove(str(data))
    return {"updated": True}
