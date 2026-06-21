# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
from lxml import etree


def coalesce_blank(value):
    return value or ''

def BenchmarkTest32641():
    user_id = request.args.get('id', '')
    data = coalesce_blank(user_id)
    if time.time() > 1000000000:
        _parser = etree.XMLParser(resolve_entities=True, no_network=False)
        etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
