# SPDX-License-Identifier: Apache-2.0
from flask import request
import asyncio
from types import SimpleNamespace


def BenchmarkTest43294():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
