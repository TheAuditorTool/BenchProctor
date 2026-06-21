# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest06976():
    multipart_value = request.form.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
