# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import asyncio
from types import SimpleNamespace


def BenchmarkTest04129(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        return redirect(str(data))
    return asyncio.run(_evasion_task())
