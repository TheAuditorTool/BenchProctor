# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from lxml import etree


@dataclass
class FormData:
    payload: str

def BenchmarkTest31815():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
