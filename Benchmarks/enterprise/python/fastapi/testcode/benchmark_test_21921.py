# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import sys
import asyncio


async def BenchmarkTest21921(request: Request):
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    async def fetch_payload():
        await asyncio.sleep(0)
        return argv_value
    data = await fetch_payload()
    checked_path = os.path.normpath(data)
    os.unlink('/var/app/data/' + str(checked_path))
    return {"updated": True}
