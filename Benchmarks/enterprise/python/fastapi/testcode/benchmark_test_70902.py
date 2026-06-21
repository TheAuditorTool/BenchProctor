# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest70902(request: Request):
    origin_value = request.headers.get('origin', '')
    data = str(origin_value).replace('\x00', '')
    os.system('echo ' + str(data))
    return {"updated": True}
