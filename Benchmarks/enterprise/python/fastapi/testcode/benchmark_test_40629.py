# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest40629(request: Request):
    user_id = request.query_params.get('id', '')
    data = user_id if user_id else 'default'
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
