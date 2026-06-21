# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import sys


async def BenchmarkTest40338(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    subprocess.Popen('echo ' + str(argv_value), shell=True).wait()
    return {"updated": True}
