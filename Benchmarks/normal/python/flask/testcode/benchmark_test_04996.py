# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest04996():
    upload_name = request.files['upload'].filename
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(upload_name).encode(), _parser)
    return jsonify({"result": "success"})
