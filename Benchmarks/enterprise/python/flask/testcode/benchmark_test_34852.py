# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest34852():
    user_id = request.args.get('id', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(user_id).encode(), _parser)
    return jsonify({"result": "success"})
