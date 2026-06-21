# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import asyncio
import importlib


def BenchmarkTest27759():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    def _primary():
        importlib.import_module(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
