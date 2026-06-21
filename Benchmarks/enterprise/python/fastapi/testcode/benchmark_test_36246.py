# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import runpy


def normalise_input(value):
    return value.strip()

async def BenchmarkTest36246(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    return {"updated": True}
