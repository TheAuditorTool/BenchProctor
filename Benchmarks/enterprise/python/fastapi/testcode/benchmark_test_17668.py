# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


async def BenchmarkTest17668(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ' '.join(str(xml_value).split())
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
