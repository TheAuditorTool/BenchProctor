# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest73957():
    xml_value = request.get_data(as_text=True)
    data = coalesce_blank(xml_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
