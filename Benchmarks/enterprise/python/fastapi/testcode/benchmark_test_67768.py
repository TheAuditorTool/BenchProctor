# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest67768(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    os.system('echo ' + str(data))
    return {"updated": True}
