# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from lxml import etree


def BenchmarkTest64744():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
