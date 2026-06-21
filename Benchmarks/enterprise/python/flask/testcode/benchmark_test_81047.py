# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest81047():
    xml_value = request.get_data(as_text=True)
    data = default_blank(xml_value)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return jsonify({"result": "success"})
