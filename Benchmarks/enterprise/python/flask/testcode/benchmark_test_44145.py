# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import asyncio


def BenchmarkTest44145():
    xml_value = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
