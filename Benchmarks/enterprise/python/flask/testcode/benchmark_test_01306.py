# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import asyncio
from types import SimpleNamespace


def BenchmarkTest01306(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
