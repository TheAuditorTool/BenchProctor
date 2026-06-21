# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


async def BenchmarkTest35560(request: Request):
    user_id = request.query_params.get('id', '')
    data = str(user_id).replace('\x00', '')
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
