# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest18733(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    os.system('echo ' + str(data))
    return {"updated": True}
