# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest31340(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    os.system('echo ' + str(data))
    return {"updated": True}
