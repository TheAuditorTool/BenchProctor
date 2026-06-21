# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import asyncio


def BenchmarkTest02111():
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    async def fetch_payload():
        await asyncio.sleep(0)
        return yaml_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
