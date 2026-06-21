# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


async def BenchmarkTest60494(request: Request):
    ua_value = request.headers.get('user-agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
