# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import asyncio


def BenchmarkTest38408():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return prop_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
