# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
from lxml import etree


def BenchmarkTest15557():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    processed = data[:64]
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(processed).encode(), _parser)
    return jsonify({"result": "success"})
