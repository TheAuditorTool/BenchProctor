# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request, jsonify
import os
import asyncio


def BenchmarkTest28232():
    raw_body = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        return redirect(str(data))
    return jsonify({"result": "success"})
