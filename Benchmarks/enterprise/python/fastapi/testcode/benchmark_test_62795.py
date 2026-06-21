# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest62795(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
