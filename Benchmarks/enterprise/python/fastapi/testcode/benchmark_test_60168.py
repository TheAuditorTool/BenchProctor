# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import sys


async def BenchmarkTest60168(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data, _sep, _rest = str(argv_value).partition('\x00')
    os.system('echo ' + str(data))
    return {"updated": True}
