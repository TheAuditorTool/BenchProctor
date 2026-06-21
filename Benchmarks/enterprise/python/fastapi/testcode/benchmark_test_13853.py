# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest13853(request: Request):
    user_id = request.query_params.get('id', '')
    data = default_blank(user_id)
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
