# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import runpy


async def BenchmarkTest34139(request: Request, field: str = Form('')):
    field_value = field
    pending = list(str(field_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
