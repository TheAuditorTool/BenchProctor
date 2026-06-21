# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import jsonify
import asyncio
from app_runtime import db


def BenchmarkTest22411():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    async def fetch_payload():
        await asyncio.sleep(0)
        return db_value
    data = asyncio.run(fetch_payload())
    def _primary():
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return jsonify({"result": "success"})
