# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import asyncio
from types import SimpleNamespace


def BenchmarkTest05136():
    xml_value = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        yaml.load(data, Loader=yaml.UnsafeLoader)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
