# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest77624():
    upload_name = request.files['upload'].filename
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
