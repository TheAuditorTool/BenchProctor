# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import runpy


async def BenchmarkTest75661(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
