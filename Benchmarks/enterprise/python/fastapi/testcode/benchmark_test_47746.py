# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest47746(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
