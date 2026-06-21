# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
from lxml import etree


def normalise_input(value):
    return value.strip()

def BenchmarkTest61782():
    multipart_value = request.form.get('multipart_field', '')
    data = normalise_input(multipart_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
