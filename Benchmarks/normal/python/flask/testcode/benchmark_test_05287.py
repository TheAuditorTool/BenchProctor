# SPDX-License-Identifier: Apache-2.0
import os
import shlex
from flask import request, jsonify
import asyncio


def BenchmarkTest05287():
    xml_value = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
