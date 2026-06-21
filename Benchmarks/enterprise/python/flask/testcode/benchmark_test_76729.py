# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from lxml import etree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest76729():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = coalesce_blank(forwarded_ip)
    eval(compile('_parser = etree.XMLParser(resolve_entities=True, no_network=False)\netree.fromstring(str(data).encode(), _parser)', '<sink>', 'exec'))
    return jsonify({"result": "success"})
