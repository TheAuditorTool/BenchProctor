# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess


async def BenchmarkTest81460(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    subprocess.run('echo ' + str(data), shell=True)
    return {"updated": True}
