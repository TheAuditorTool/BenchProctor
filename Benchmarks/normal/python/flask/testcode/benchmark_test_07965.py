# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest07965():
    cookie_value = request.cookies.get('session_token', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(cookie_value).encode(), _parser)
    return jsonify({"result": "success"})
