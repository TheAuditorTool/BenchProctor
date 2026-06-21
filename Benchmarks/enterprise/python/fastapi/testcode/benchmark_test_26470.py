# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import sys


async def BenchmarkTest26470(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    def normalize(value):
        return value.strip()
    data = normalize(argv_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
