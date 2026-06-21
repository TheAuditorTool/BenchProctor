# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import sys


async def BenchmarkTest43759(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    if argv_value:
        data = argv_value
    else:
        data = ''
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
