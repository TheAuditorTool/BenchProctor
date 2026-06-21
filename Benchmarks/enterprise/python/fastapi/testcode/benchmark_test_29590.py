# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import sys


async def BenchmarkTest29590(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    parts = str(argv_value).split(',')
    data = ','.join(parts)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
