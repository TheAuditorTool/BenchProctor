# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from lxml import etree
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest27583():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    request_state['last_input'] = comment_value
    data = request_state['last_input']
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
