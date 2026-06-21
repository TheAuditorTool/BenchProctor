# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08325(request: Request):
    user_id = request.query_params.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    request.session['user'] = str(data)
    return {"updated": True}
