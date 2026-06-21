# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest81096(request: Request):
    referer_value = request.headers.get('referer', '')
    data = normalise_input(referer_value)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
