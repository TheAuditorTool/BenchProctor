# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio
from app_runtime import auth_check


def BenchmarkTest65932():
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
