# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import runpy


async def BenchmarkTest20401(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
