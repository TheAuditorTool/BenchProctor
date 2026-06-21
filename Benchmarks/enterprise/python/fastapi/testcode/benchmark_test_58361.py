# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest58361(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    os.system('echo ' + str(data))
    return {"updated": True}
