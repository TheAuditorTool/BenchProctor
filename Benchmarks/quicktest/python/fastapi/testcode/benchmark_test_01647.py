# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import sys


async def BenchmarkTest01647(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    def normalize(value):
        return value.strip()
    data = normalize(argv_value)
    os.system('echo ' + str(data))
    return {"updated": True}
