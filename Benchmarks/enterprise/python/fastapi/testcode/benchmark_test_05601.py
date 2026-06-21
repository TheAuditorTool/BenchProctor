# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
from urllib.parse import unquote


async def BenchmarkTest05601(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
