# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import os


async def BenchmarkTest51179(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        return RedirectResponse(url=str(data))
    return {"updated": True}
