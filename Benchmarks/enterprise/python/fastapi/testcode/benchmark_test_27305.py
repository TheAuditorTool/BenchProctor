# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest27305(request: Request):
    host_value = request.headers.get('host', '')
    reader = make_reader(host_value)
    data = reader()
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
