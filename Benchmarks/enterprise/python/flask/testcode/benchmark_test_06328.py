# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from lxml import etree


def BenchmarkTest06328():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
