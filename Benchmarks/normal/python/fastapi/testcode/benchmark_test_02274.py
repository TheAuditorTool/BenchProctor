# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


async def BenchmarkTest02274(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(cookie_value) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
