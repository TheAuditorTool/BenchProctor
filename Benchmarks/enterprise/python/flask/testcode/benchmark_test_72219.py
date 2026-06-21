# SPDX-License-Identifier: Apache-2.0
import logging
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest72219():
    multipart_value = request.form.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return jsonify({"result": "success"})
