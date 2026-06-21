# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import runpy


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest07787(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
