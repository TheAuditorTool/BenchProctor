# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import runpy


async def BenchmarkTest31503(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
