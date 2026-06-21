# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import asyncio
from types import SimpleNamespace


def BenchmarkTest15893(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        return Markup('<img src="' + str(data) + '">')
    return asyncio.run(_evasion_task())
