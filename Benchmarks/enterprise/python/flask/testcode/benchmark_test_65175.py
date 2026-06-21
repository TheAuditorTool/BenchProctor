# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from lxml import etree
from app_runtime import db


def ensure_str(value):
    return str(value)

def BenchmarkTest65175():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = ensure_str(db_value)
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
