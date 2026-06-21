# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import sys


async def BenchmarkTest75389(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = (lambda v: v.strip())(argv_value)
    os.system('echo ' + str(data))
    return {"updated": True}
