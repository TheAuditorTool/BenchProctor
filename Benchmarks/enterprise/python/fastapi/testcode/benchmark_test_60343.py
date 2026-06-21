# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import asyncio
import importlib
import sys


async def BenchmarkTest60343(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = await fetch_payload()
    eval(compile("sys.path.insert(0, str(data))\nimportlib.import_module('report_renderer')", '<sink>', 'exec'))
    return {"updated": True}
