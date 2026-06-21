# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from lxml import etree


@dataclass
class FormData:
    payload: str

def BenchmarkTest04499():
    referer_value = request.headers.get('Referer', '')
    data = FormData(payload=referer_value).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
