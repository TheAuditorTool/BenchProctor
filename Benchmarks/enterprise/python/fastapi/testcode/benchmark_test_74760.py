# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest74760(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    auth_check('user', data)
    return {"updated": True}
