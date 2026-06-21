# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest04579(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    os.system('echo ' + str(data))
    return {"updated": True}
