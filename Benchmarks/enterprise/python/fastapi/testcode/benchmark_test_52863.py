# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest52863(request: Request):
    upload_name = (await request.form()).get('upload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    eval(compile('eval(str(data))', '<sink>', 'exec'))
    return {"updated": True}
