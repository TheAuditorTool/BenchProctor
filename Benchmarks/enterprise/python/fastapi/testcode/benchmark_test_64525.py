# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest64525(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = str(header_value).replace('\x00', '')
    os.remove(str(data))
    return {"updated": True}
