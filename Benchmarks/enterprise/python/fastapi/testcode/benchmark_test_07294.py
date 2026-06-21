# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest07294(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
