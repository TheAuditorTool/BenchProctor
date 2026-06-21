# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest68448(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    os.system('echo ' + str(data))
    return {"updated": True}
