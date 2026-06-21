# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import sys


async def BenchmarkTest59327(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = ' '.join(str(argv_value).split())
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
