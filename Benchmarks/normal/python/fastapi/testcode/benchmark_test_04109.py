# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


async def BenchmarkTest04109(request: Request):
    user_id = request.query_params.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
