# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request
import asyncio


def BenchmarkTest67653():
    host_value = request.headers.get('Host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    async def _evasion_task():
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    return asyncio.run(_evasion_task())
