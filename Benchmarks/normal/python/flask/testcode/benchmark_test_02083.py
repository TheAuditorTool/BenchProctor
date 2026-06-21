# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from lxml import etree


@dataclass
class FormData:
    payload: str

def BenchmarkTest02083():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
