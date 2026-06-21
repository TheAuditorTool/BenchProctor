# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest46784():
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return jsonify({"result": "success"})
