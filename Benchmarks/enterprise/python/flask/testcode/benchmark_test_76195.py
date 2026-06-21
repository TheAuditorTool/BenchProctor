# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
from types import SimpleNamespace
from lxml import etree


def BenchmarkTest76195():
    raw_body = request.get_data(as_text=True)
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
