# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import asyncio


def BenchmarkTest76903():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return config_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
