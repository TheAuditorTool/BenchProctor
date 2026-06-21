# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import sys


async def BenchmarkTest38045(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    if argv_value:
        data = argv_value
    else:
        data = ''
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
