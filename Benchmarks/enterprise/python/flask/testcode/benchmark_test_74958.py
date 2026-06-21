# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from lxml import etree
from app_runtime import db


def BenchmarkTest74958():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    def normalize(value):
        return value.strip()
    data = normalize(db_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
