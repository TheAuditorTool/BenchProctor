# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest58002(request: Request):
    auth_header = request.headers.get('authorization', '')
    os.system('echo ' + str(auth_header))
    return {"updated": True}
