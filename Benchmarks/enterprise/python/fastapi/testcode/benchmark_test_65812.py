# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
from starlette.responses import HTMLResponse
import os
from types import SimpleNamespace


async def BenchmarkTest65812(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse('<script src="' + str(data) + '"></script>')
    return {"updated": True}
