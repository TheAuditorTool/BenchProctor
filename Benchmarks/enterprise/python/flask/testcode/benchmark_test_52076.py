# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from lxml import etree


@dataclass
class FormData:
    payload: str

def BenchmarkTest52076():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
