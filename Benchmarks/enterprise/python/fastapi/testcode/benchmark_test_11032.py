# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest11032(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
