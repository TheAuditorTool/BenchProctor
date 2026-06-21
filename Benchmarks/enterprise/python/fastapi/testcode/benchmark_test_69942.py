# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69942(request: Request):
    upload_name = (await request.form()).get('upload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    result = 100 / int(str(data))
    return {"updated": True}
