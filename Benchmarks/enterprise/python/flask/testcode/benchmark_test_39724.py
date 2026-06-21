# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify
import asyncio


def BenchmarkTest39724():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    eval(compile('tree = etree.fromstring(b\'<users><user name="admin"/></users>\')\ntree.xpath(\'/users/user[name="\' + str(data) + \'"]\')', '<sink>', 'exec'))
    return jsonify({"result": "success"})
