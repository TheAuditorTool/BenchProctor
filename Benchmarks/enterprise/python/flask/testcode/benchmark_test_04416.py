# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import asyncio


def BenchmarkTest04416():
    upload_name = request.files['upload'].filename
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return jsonify({"result": "success"})
