# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest48820(request: Request):
    user_id = request.query_params.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return {"updated": True}
