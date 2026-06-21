# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10914(request: Request):
    upload_name = (await request.form()).get('upload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    processed = data[:64]
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(processed))
    return {"updated": True}
