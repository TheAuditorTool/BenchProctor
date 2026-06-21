# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import sys


async def BenchmarkTest30365(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    if argv_value:
        data = argv_value
    else:
        data = ''
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
