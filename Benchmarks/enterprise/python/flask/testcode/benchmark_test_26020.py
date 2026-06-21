# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import os
import asyncio


def BenchmarkTest26020():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
