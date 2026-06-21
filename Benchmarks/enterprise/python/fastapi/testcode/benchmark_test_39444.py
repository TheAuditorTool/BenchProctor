# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest39444(request: Request):
    path_value = request.path_params.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
