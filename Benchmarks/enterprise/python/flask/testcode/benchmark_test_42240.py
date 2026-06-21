# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import time
import asyncio


def BenchmarkTest42240():
    user_id = request.args.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
