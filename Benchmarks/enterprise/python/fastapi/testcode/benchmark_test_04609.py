# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import time


async def BenchmarkTest04609(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
