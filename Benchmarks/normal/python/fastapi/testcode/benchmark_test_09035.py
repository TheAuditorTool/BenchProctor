# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import runpy


async def BenchmarkTest09035(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    if time.time() > 1000000000:
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
