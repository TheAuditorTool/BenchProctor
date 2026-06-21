# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import asyncio


def BenchmarkTest08784():
    raw_body = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    async def _evasion_task():
        yaml.load(data, Loader=yaml.UnsafeLoader)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
