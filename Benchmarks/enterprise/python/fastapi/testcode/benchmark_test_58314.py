# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest58314(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
