# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
from lxml import etree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest81100():
    header_value = request.headers.get('X-Custom-Header', '')
    data = handle(header_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
