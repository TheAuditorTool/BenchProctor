# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest79265(request: Request):
    upload_name = (await request.form()).get('upload', '')
    reader = make_reader(upload_name)
    data = reader()
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
