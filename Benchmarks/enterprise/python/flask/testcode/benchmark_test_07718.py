# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import request, jsonify
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest07718():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    async def _evasion_task():
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
