# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
from lxml import etree


def to_text(value):
    return str(value).strip()

def BenchmarkTest78296():
    auth_header = request.headers.get('Authorization', '')
    data = to_text(auth_header)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
