# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def BenchmarkTest06979():
    multipart_value = request.form.get('multipart_field', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(multipart_value).encode(), _parser)
    return jsonify({"result": "success"})
