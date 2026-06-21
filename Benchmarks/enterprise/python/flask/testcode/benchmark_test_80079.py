# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import asyncio


def BenchmarkTest80079():
    host_value = request.headers.get('Host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
