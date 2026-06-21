# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


async def BenchmarkTest04678(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(raw_body) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
