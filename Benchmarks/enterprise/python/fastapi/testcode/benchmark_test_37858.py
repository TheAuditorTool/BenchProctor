# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest37858(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return {"updated": True}
