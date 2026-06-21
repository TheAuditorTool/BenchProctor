# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest50197(request: Request):
    path_value = request.path_params.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    processed = data[:64]
    data = bytearray(int(processed) if str(processed).isdigit() else 0)
    return {"updated": True}
