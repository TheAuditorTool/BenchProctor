# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import sys


async def BenchmarkTest66963(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data, _sep, _rest = str(argv_value).partition('\x00')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
