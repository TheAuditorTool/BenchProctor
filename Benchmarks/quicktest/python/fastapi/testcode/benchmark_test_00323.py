# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest00323(request: Request):
    stdin_value = input('input: ')
    data = (lambda v: v.strip())(stdin_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return {"updated": True}
