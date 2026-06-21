# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
import runpy


@dataclass
class FormData:
    payload: str

async def BenchmarkTest31283(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
