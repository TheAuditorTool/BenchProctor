# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import runpy


async def BenchmarkTest01552(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
