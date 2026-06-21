# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from types import SimpleNamespace
from lxml import etree


def BenchmarkTest13256():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ns = SimpleNamespace(payload=json_value)
    data = getattr(ns, 'payload')
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return jsonify({"result": "success"})
