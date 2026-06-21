# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


def to_text(value):
    return str(value).strip()

async def BenchmarkTest71636(request: Request):
    path_value = request.path_params.get('id', '')
    data = to_text(path_value)
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    await _evasion_task()
    return {"updated": True}
