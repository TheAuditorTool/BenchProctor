# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest00853(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
