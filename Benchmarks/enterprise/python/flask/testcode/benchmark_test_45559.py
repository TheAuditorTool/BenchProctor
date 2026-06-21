# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os
import asyncio


def BenchmarkTest45559():
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    if os.environ.get("APP_ENV", "production") != "test":
        return '<script src="' + str(data) + '"></script>', 200, {'Content-Type': 'text/html'}
    return jsonify({"result": "success"})
