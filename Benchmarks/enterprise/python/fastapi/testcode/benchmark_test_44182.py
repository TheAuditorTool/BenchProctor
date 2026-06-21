# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


async def BenchmarkTest44182(request: Request):
    path_value = request.path_params.get('id', '')
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(path_value) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
