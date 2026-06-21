# SPDX-License-Identifier: Apache-2.0
import logging
from flask import jsonify
import os
import asyncio


def BenchmarkTest22298():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return dotenv_value
    data = asyncio.run(fetch_payload())
    logging.info('User action: ' + str(data))
    return jsonify({"result": "success"})
