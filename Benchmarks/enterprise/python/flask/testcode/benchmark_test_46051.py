# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import asyncio


def BenchmarkTest46051():
    field_value = request.form.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
