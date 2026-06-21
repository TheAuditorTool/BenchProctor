# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
from types import SimpleNamespace
from lxml import etree


def BenchmarkTest72693():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
